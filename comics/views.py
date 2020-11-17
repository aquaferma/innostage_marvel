from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .serializers import UserComicSerializer
from .marvel_api.marvel_methods import get_comics, get_comic
from master import models
from django.conf import settings
from math import ceil


class Comic(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'comic.html'
    authentication_classes = [SessionAuthentication]

    def get(self, request, id):
        error, data = get_comic(id)
        if error:
            return Response({"error": data})

        return Response({"comic": data['data']['results'][0], 
                         "is_saved": comic_is_saved(request.user, id)})

    def post(self, request, id):
        error, data = get_comic(id)
        if error:
            return Response({"error": data})

        serializer = UserComicSerializer(data=data['data']['results'][0])
        # print(data['data']['results'][0])
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(request.user) 
            return Response({"message": "Сохранено"})
        else:
            print(serializer.errors)
            return Response({"error": "Validation error"})


class Marvel(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'comics.html'

    def get(self, request, page=1):

        title = request.GET.get("title")
        
        error, data = get_comics(title, page)
        # print(data)

        if error:
            return Response({"error": data})

        pages = range(1, ceil(data['data']['total']/settings.COMICS_PAGE_COUNT))
        print(pages)
        
        return Response({"comics": data['data']['results'], "search_title": title or "", "pages": pages})


def comic_is_saved(user, comic_id):
    return models.UserComics.objects.filter(user=user, comics__comic_id=comic_id).exists()