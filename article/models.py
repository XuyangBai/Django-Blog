#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    #auto_now_add设置True表示自动设置对象增加时间
    content = models.TextField(blank = True, null = True)  #博客文章正文

    #python2使用__unicode__, python3使用__str__
    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']