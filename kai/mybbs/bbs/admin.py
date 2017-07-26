from django.contrib import admin
from bbs import models


'''
admin页面定制化
'''
class bbs_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','view_count','createdtime',)
    list_filter = ('createdtime',)
    search_fields = ('title','author__user__username')

    def signature(self,obj):
        return obj.author.signature

admin.site.register(models.bbs,bbs_admin)
admin.site.register(models.bbs_user)
admin.site.register(models.category)