from django.urls import path, re_path
from django.http import HttpResponse, HttpRequest

def home(request: HttpRequest):
    return HttpResponse("/")

def page1(request: HttpRequest):
    return HttpResponse("/page1")

def not_found(request: HttpRequest):
    return HttpResponse("404 Not Found")

urlpatterns = [
    path('', home),
    path('page1', page1),
    re_path('', not_found), # re_path => regex match
]
