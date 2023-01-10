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


def post_detail(request,pk):
    try:
        post = get_pbject_or_404(Post,pk=pk)
        c_number = len(comment.objects.filter(post_id=pk))
    except post.DoesNotExist:
        raise Http404("detial for this post deost not exist")
    return render(request,"blog/post_detail.html",{'post': post,'c_number':c_number})


def post_comment(request,pk):
    try:
        comments = comment.object.filter(post_id=pk)
        post_id=pk
    except comments.DoesNotExist:
        raise Http404("comments for this post does not exist")
    return render(request,"blog/post_comment.html", {'comments':comments, 'post_id':post_id})

def add_comment(request,pk):
    if request.method == "POST":
        form = CommentForm(request.Post)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.name = request.POST['name']
            comment.comment = request.POST['comment']
            comment.post_id = pk
            comment.save
            return redirect('post_detail', pk=pk)
        else:
            form = CommentForm()
        return render(request,"blog/post_comment.html", {'comments':comments, 'form':form} )



