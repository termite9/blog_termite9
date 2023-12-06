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
    posts = list(reversed(Post.objects.all()))
    #
    # posts = Post.objects.all()
    # comment_form = CommentForm()
    context = {
        "posts": posts,
        #            "comment_form" : comment_form,
    }
    return render(request, "index.html", context)


def post_list(request):

    posts = list(reversed(Post.objects.all()))
    posts_free = list((Post.objects.filter(writer='').order_by('-pk')))
    page = int(request.GET.get('page', 1))

    # paginator = Paginator(posts, 5)
    # page_obj_posts = paginator_posts.get_page(page)
    # page_obj = paginator.get_page(page)
    # context = {
    #     "posts": page_obj,
    #     "posts_free":posts_free,
    # }
    paginator_posts = Paginator(posts, 5)
    page_obj_posts = paginator_posts.get_page(page)

    paginator_posts_free = Paginator(posts_free, 5)
    page_obj_posts_free = paginator_posts_free.get_page(page)

    context = {
        "posts": page_obj_posts,
        "posts_free": page_obj_posts_free,
    }

    return render(request, 'post_list.html',  context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)


def post_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        write_date = request.POST["write_date"]
        content = request.POST["content"]
        writer = request.POST["writer"]
        if "thumbnail" in request.FILES:
            thumbnail = request.FILES["thumbnail"]
            post = Post.objects.create(
                title=title,
                write_date=write_date,
                content=content,
                thumbnail=thumbnail,
                writer=writer,
            )

        else:
            post = Post.objects.create(
                title=title,
                write_date=write_date,
                content=content,
                writer=writer,
            )
        return redirect(f"/posts/{post.id}")

    else:
        return render(request, "post_add.html")
