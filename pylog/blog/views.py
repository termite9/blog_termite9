from django.shortcuts import render, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
# Create your views here.
# from posts.forms import CommentForm
from django.shortcuts import render
from users.forms import LoginForm

# Create your views here.
def index(request):

    # if not request.user.is_authenticated:
     # return redirect("/posts/")
    # form = LoginForm()
    # context = {
    #     "form": form,
    # }
    #
    # posts = Post.objects.all()
    # comment_form = CommentForm()
    # context = {
    #     "posts" : posts,
    #            "comment_form" : comment_form,
    #            }
    return render(request, "/users/login.html")




def post_list(request):

    posts = list(reversed(Post.objects.all()))
    # posts=reversed(posts1)
    page = int(request.GET.get('page', 1))

    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)
    context = {
        "posts": page_obj,
    }
    # context = {
    #     "posts": posts,
    # }
    # return render(request, 'post_list.html',  context)

    return render(request, 'post_list.html',  context)
    # posts1=Post.objects.all()
    # posts=reversed(posts1)
    # context = {
    #     "posts": posts,
    # }
    # return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method =="POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context = {
        "post" : post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST" :
        title=request.POST["title"]
        write_date=request.POST["write_date"]
        content=request.POST["content"]
        if "thumbnail" in request.FILES:
            thumbnail = request.FILES["thumbnail"]
            post = Post.objects.create(
            title=title,
            write_date=write_date,
            content=content,
            thumbnail=thumbnail,
            )

        else:
            post = Post.objects.create(
                title=title,
                write_date=write_date,
                content=content,
            )
        return redirect(f"/posts/{post.id}")


    else:
       return render(request, "post_add.html")

