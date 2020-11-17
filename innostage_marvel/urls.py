from django.contrib import admin
from django.urls import path, include
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('marvel/', include('comics.urls')),
    path('master/', include('master.urls')),
    path('', main),
]
