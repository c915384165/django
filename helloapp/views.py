from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello World! I am coming...")


def hello_test(request):
    return render(request, "test_2.html")


def mission1(request):
    return render(request, "mission1.html")
