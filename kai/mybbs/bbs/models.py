from django.db import models
from django.contrib.auth.models import User     #导入django自带的用户认证表



"""
创建bbs相关的表
"""
class bbs(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True)
    content = models.TextField()
    author = models.ForeignKey('bbs_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    createdtime = models.DateTimeField()
    updatetime = models.DateTimeField()

    def __unicode__(self):
        return self.title

class comment(models.Model):
    pass

class category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    admin = models.ForeignKey('bbs_user')


class bbs_user(models.Model):
    user = models.OneToOneField(User)
    singnature = models.CharField(max_length=128,default='this guy is too lazy to levave anything here.')
    photo = models.ImageField()
    photo = models.ImageField(upload_to="upload_imgs/",default="upload_imgs/user_1.jpg")

    def __unicode__(self):
        return self.user.username