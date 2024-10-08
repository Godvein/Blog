from django.urls import path
from blogmain import views

urlpatterns = [
    path('', views.home, name = "home")
]