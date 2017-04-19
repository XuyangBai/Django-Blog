#coding=utf-8
"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import article.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article.views.home),
    url(r'^(?P<my_args>\d+)/$', article.views.detail, name='detail'),
]
#url()函数有四个参数, 两个是必须的:regex和view,
#两个可选的:kwargs和name
#kwargs任意关键字参数可传一个字典至目标view
#name命名你的 URL, 使url在 Django 的其他地方使用, 特别是在模板中

#^(?P<my_args>\d+)/$这个正则表达式的意思是将传入的一位或者多位数字作为参数传递到views中的detail作为参数, 其中?P<my_args>定义名称用于标识匹配的内容