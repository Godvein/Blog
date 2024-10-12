from django.urls import path
from blogmain import views
from .views import blogList,blogDetail,userblogList
urlpatterns = [
    path('', blogList.as_view(), name = "home"),
    path('blogdetail/<int:pk>/', blogDetail.as_view(), name = "detail"),
    path('createpost/', views.createblog, name = "createpost"),
    path('deletepost/<int:id>', views.deleteblog, name = "deletepost"),
    path('updatepost/<int:id>', views.updateblog, name = "updatepost"),
    path('userblogs/<str:username>', userblogList.as_view(), name = "userbloglist")
]