from django.urls import path
from .views import deployment_django

urlpatterns = [
    path('', deployment_django, name='deployment_django'),
]