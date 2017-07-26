
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.contrib import auth
import models


'''
首页的函数
'''
def index(requset):

    bbs_list = models.bbs.objects.all()
    return render_to_response('index.html',{'bbs_list': bbs_list})

'''
具体内容页的函数
'''
def detail(requset,bbs_id):

    bbs= models.bbs.objects.get(id=bbs_id)

    return render_to_response('bb_tmp.html',{'bbs_obj':bbs})