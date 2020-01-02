from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponse, StreamingHttpResponse
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


# FileResponse 类型
def homeproc3(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/pythonlogo.jpg", "rb"))
    # 两个标记：
    # "Content-type" 指定文件类型
    response['Content-type'] = 'application/octet-stream'
    # "Content-Disposition" 指定文件的名称
    response['Content-Disposition'] = 'attachment;filename="pylogo.png"'
    return response


# 文件一次性响应 HttpResponse 方式：
def file_download(request):
    # do something...
    with open('data.txt') as f:
        c = f.read()
    return HttpResponse(c)


# StreamingHttpResponse 方式
def big_file_download(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    fname = "data.txt"
    response = StreamingHttpResponse(file_iterator(fname))
    return response
