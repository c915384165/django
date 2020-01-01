from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponse
import os
# Create your views here.


def homeproc(request):
    return HttpResponse("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")


def homeproc2(request):
    response = HttpResponse()
    response.write("<h1>这是首页，具体功能访问<a href='./msggate'>这里</a></h1>")
    response.write("<h1>这是第二行</h1>")
    return response


def homeproc1(request):
    response = JsonResponse({'key': 'value'})
    return response


def homeproc3(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/pythonlogo.jpg", "rb"))
    response['Content-type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="pylogo.png"'
    return response
