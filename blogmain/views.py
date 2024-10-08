from django.shortcuts import render
from .models import blogs
# Create your views here.
def home(request):
    blog = {
        "post" : blogs.objects.all()
    }
    
    return render(request, "home.html", blog)