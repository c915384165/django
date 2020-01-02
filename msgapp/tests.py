from django.test import TestCase
import json
import os

# Create your tests here.
# Templates 的用法
# def pgproc(request):
#     template = Template("<h1>这个程序的名字是{{ name }}</h1>")
#     cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     c = json.load(cwd + "/msgapp/test.json")
#     a = c.read()
#     context = Context(a)
#     # context = Context({"name": "实验平台"})
#     return HttpResponse(template.render(context))

cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = open(cwd + "/msgapp/test.json", "rt")
j = json.load(f)
print(j)
