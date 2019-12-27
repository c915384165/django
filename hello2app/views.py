from django.shortcuts import render

# Create your views here.


def hello(request):
    # render
    return render(request, "PYC01-HTMLJSDemo.html")

