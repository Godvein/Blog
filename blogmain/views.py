from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import blogs
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from django.core.management import call_command


def create_superuser_view(request):
    call_command('create_superuser')
    return HttpResponse('Superuser created.')

#object based view
class blogList(ListView):
    model = blogs
    template_name = "blogmain/home.html"
    context_object_name = 'post'
    ordering = ["-date_created"]
    paginate_by = 6
    

class userblogList(ListView):
    model = blogs
    template_name = "blogmain/user_post.html"
    context_object_name = 'post'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get("username"))
        return blogs.objects.filter(user = user).order_by("-date_created")
    
    
class blogDetail(DetailView):
    model = blogs

@login_required(login_url="/login/")
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
    