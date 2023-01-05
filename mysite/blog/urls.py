""" import from various files and midleuse """
from django.contrib import admin
from django.urls import path
from .views import index,post_list, post_detail,post_comment,add_comment
from django.conf import settings

urlpatterns = [
    path('',index),
    path('posts/',post_list),
    path('posts/(?P<pk>[0-9]+)/',post_detail),
    path('posts/(?P<pk>[0-9]+)/comment/',post_comment),
    path('posts/(?P<pk>[0-9]+)/comment/add_comment',add_comment),
]