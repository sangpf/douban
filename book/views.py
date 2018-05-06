# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers
from models import BookInfo

def index(request):
    booklist = BookInfo.objects.all()
    template = loader.get_template('book/index.html')
    context = RequestContext(request, {'booklist': booklist})
    return HttpResponse(template.render(context))

def detail(reqeust, id):
    book = BookInfo.objects.get(pk=id)
    template = loader.get_template('book/detail.html')
    context = RequestContext(reqeust, {'book': book})
    return HttpResponse(template.render(context))

def list_book(request):
    # id = request.GET['id']
    # title = request.GET['title']
    # title = request.GET.get('title','title default')  # 有默认值
    id = request.GET.get('id')
    title = request.GET.get('title')

    book_list = BookInfo.objects.all()
    if id != None:
        book_list = book_list.filter(pk=id)
    if title != None:
        book_list = book_list.filter(btitle=title)

    # project_list = Project.objects.filter(invId__exact=id).filter(title=title)
    book_list_serialize = serializers.serialize('json', book_list)
    return HttpResponse(book_list_serialize)
    # context = {'id':id, 'title':title}
    # return JsonResponse(context)


