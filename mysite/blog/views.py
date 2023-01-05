from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from datetime import datetime
#from .models import Post,comment
#from .forms import CommentForm
from django.http import HttpResponse
from django.http import Http404





def index(request):
    context = {
        'date':datetime.now(),
        'tittle':'Home page'
    }
    return render(request,"blog/index.html", context)

def post_list(request):
    try:
        posts = Post.pbject.all()
    except Post.DoesNotExist:
        raise Http404("Post deost not exist")
    return render(request,"blog/post_list.html", context, {'posts': posts})


def post_detail(request):
    try:
        posts = Post.pbject.all()
    except Post.DoesNotExist:
        raise Http404("Post deost not exist")
    return render(request,"blog/post_detail.html", context, {'posts': posts})

def post_comment(request):
    try:
        posts = Post.pbject.all()
    except Post.DoesNotExist:
        raise Http404("Post deost not exist")
    return render(request,"blog/post_comment.html", context, {'posts': posts})

def add_comment(request):
    try:
        posts = Post.pbject.all()
    except Post.DoesNotExist:
        raise Http404("Post deost not exist")
    return render(request,"blog/add_comment.html", context, {'posts': posts})



