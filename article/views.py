#coding=utf-8
from django.shortcuts import render
from article.models import  Article
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    print post_list
    return render(request, 'home.html', {'post_list': post_list})

#render()函数中第一个参数是request 对象, 第二个参数是一个模板名称，第三个是一个字典类型的可选参数.
#它将返回一个包含有给定模板根据给定的上下文渲染结果的 HttpResponse对象


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    print post
    return render(request, 'post.html', {'post' : post})