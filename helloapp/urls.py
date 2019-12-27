from django.urls import path
# 从当前app .
from . import views

# 添加app的本地路由
urlpatterns = [
    path('', views.hello),
    path('test/', views.hello_test)
]
