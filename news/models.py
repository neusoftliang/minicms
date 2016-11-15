# -*- coding: utf-8 -*-
from django.db import models
#兼容Python2 和Python3
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
# Create your models here.
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址',max_length=256,db_index=True)
    intro = models.TextField('栏目简介',default='')
    def __str__(self):
        return self.name

    # 通过一个内嵌类
    # "class Meta"
    # 给你的
    # model
    # 定义元数据, 类似下面这样:
    # verbose_name
    # 是该对象的一个可读性更好的唯一名字:
    #
    # verbose_name = "pizza"
    #
    # 若未提供该选项, Django
    # 则会用一个类名字的
    # munged
    # 版本来代替: CamelCase
    # becomes
    # camel
    # case.
    #
    # verbose_name_plural
    # 对象名字的复数:
    #
    # verbose_name_plural = "stories"
    #
    # 若未提供该选项, Django
    # 会使用
    # verbose_name + "s".
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']
@python_2_unicode_compatible
class Article(models.Model):
    #ManyToManyField多对多关系
    column = models.ManyToManyField(Column,verbose_name='归属栏目')
    title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256,db_index=True)
    #ForeginKey一对多关系
    author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者')
    content = UEditorField('内容',default='',blank=True)
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'