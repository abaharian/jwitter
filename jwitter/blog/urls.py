from django.urls import path

from . import views
from blog.views import PostList
urlpatterns = [
    path('', views.index, name = "index"),
    path('posts', PostList.as_view())
]