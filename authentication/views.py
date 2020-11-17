from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import AuthenticationSeializer
from django.contrib.auth import authenticate, login, logout


class Authentication(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'authentication.html'

    def get(self, request):
        return Response({'serializer': AuthenticationSeializer()})

    def post(self, request):
        serializer = AuthenticationSeializer(data=request.data)
        
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)

            if not user:
                return Response({'serializer': AuthenticationSeializer(), 
                                 'error': 'Неправильный логин и\или пароль'})
            login(request, user)
            return HttpResponseRedirect(reverse('master'))

        return Response({'serializer': serializer})

        
class Logout(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            logout(request)

        return HttpResponseRedirect('/')
        
