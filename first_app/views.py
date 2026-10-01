from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def deployment_django(request):
    return HttpResponse('Deployment Django !!!')

