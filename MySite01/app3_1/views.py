from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # we want to display html file
    # rendering html document
    # return HttpResponse("Hello from App3")
    return render(request, 'app3_1/First.html')

def get_value(request):
    var1 = request.GET.get('var1') # getting value from URL (Address Bar)
    # return HttpResponse("Full Name : "+str(var1))# display on browser
    context = {'value1': var1}
    return render(request, 'app3_1/Second.html', context) # Sending value to HTML Template (HTML Document)
