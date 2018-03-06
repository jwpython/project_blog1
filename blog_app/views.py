from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models
from django.http import Http404
# Create your views here.

def Test(request):
    # return HttpResponse("just a test")
    return render(request, 'blog_app/test.html', {'current_time': datetime.datetime.now()})

def home(request):
    post_list = models.Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog_app/home.html',{'post_list':post_list})


def Detail(request,id):
    try:
        post = models.Article.objects.get(id=str(id))
    except models.Article.DoesNotExist:
        raise Http404
    return render(request,'blog_app/post.html',{'post':post})