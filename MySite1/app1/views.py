from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<b>Hello form Broadway</b>")
