from django.urls import path

from . import views
from blog.views import PostList, PostDetail
urlpatterns = [
    path('', views.index, name = "index"),
    path('posts', PostList.as_view()),
    path('posts/<int:id>', PostDetail.as_view())
]