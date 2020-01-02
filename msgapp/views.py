from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponse, StreamingHttpResponse
from django.template import Template, Context
import os
import json


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


# Templates 的用法
def pgproc(request):
    template = Template("<h1>这个程序的名字是{{ name }}</h1>")
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    f = open(cwd + "/msgapp/test.json", "rt")
    j = json.load(f)
    context = Context(j)
    # context = Context({"name": "实验平台"})
    return HttpResponse(template.render(context))


"""
1）从类中导入模版类和context类
2）模版，和文字
3）渲染
通过模版方法可以将数据与模版结合起来，生成动态的网页。渲染：链接数据与模版。
模版：即半成品，这里指有动态缺口的html文件。
数据：json格式的词典。
"""
