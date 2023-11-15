from django.shortcuts import render, redirect
# from posts.models import Post
# from posts.forms import CommentForm
from django.shortcuts import render

# Create your views here.
def feeds(request):
    if not request.user.is_authenticated:
        return redirect("/posts/")
    # posts = Post.objects.all()
    # comment_form = CommentForm()
    # context = {
    #     "posts" : posts,
    #            "comment_form" : comment_form,
    #            }
    return render(request, "post_list.html")
