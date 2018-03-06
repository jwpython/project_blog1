#coding:utf8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test/',views.Test,name="blog_test"),
    url(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_app_Detail"),
    url(r'^home/', views.home, name="blog_app_home"),
]