from django.shortcuts import render

from django.http import HttpResponse # import HttpResponse

def index(request):
    return HttpResponse("Hello from index of views.py of app1_1")

def f1(request):
    return HttpResponse("Hello world of Django!")
