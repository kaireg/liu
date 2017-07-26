#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,HttpResponseRedirect
import models

def index(request):
    return render(request,'index.html')

def list(requsst):

    tests = models.Employee.objects.order_by("-d").all

    return render_to_response('list.html',{"test":tests})

def add(requset):
    #判断表单是否有数据传入
    if requset.method == "POST":

        #获取表单中传入的数据
        title = requset.POST.get('title',None)
        content = requset.POST.get('content',None)

        #将数据写入数据库
        new = models.Employee(title=title,content=content)
        new.save()

        #跳转
        return HttpResponseRedirect('/list')

    return render_to_response('add.html',{'mod_str':requset.method})