from django.urls import path, include
from authentication import views


urlpatterns = [
    path('', views.Authentication.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
]