from django.shortcuts import render


# Create your views here.
def template_1(request):
    return render(request, "Template1.html")


def template_2(request):
    return render(request, "Template2.html")