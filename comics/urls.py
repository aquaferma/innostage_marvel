from django.urls import path, include
from .views import Marvel, Comic


urlpatterns = [
    # path('', Marvel.as_view(), name='comics'),
    path('<int:page>/', Marvel.as_view(), name='comics'),
    path('comic/<int:id>', Comic.as_view(), name='comic'),
]