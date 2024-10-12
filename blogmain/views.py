from django.shortcuts import render,redirect
from .models import blogs
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView

#object based view
class blogList(ListView):
    model = blogs
    template_name = "blogmain/home.html"
    context_object_name = 'post'
    ordering = ["-date_created"]
    paginate_by = 6
    
class blogDetail(DetailView):
    model = blogs

def createblog(request):
    if request.method == "POST":
        user = User.objects.get(id = request.user.id)
        title = request.POST.get("title")
        post = request.POST.get("content")
        blog = blogs(user = user, title = title, post = post)
        blog.save()
        return redirect("home")
    return render(request, "blogmain/createblog.html")

def deleteblog(request, id):
    blog = blogs.objects.get(id = id)
    blog.delete()
    return redirect("home")

def updateblog(request, id):

    blog = blogs.objects.get(id = id)
    post = {
        "blog": blog
    }
    if request.method == "POST":
        title = request.POST.get("title")
        post = request.POST.get("content")
        blog.title = title
        blog.post = post
        return redirect("home")
    return render(request, "blogmain/updateblog.html", post)
    