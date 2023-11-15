from django.shortcuts import redirect,render


def index(request):
    if request.user.is_authenticated:
        pass
        # return redirect("/posts/")
    # else:
    #     return redirect("/")
    return render(request, "index.html")


