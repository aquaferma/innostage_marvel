from django.urls import path, include
from .views import Master
   
    
urlpatterns = [
    path('', Master.as_view(), name='master'),
]