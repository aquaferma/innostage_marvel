from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .models import UserComics


class Master(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    authentication_classes = [SessionAuthentication, ]
    template_name = 'user_comics.html'

    def get(self, request):
        user_comics = UserComics.objects.filter(user=request.user)
        if user_comics.exists():
            return Response({"comics": user_comics[0].comics.all()})
        
        return Response({"error": "Нет сохраненных комиксов"})


