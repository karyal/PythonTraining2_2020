from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from Krishna!")# Return text/String

def load_html(request):
    return render(request, 'app1/First.html') # Load and return html file