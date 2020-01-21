# -*-coding:utf-8-*-

from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target','nickname','content','website','created_time')




