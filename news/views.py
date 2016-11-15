from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def column_detail(request,column_slug):
    return HttpResponse('column slug:' + column_slug)
def article_detail(request,article_slug):
    return HttpResponse('article_slug:' + article_slug)
def index(request):
    return HttpResponse(u'自强学堂')
