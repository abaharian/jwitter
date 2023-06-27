from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from rest_framework.views import APIView
from blog.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    ret = '<body>'
    all_posts = Post.objects.all()
    for item in all_posts:
        ret = ret + '<p>' + item.text + '</p>'
    ret = ret + '</body>'
    return HttpResponse(ret)

class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serialized = PostSerializer(posts, many = True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    def post(self, request, format = None):
        deserialized = PostSerializer(data = request.data)
        if deserialized.is_valid():
            deserialized.save()
            return Response(deserialized.data, status=status.HTTP_201_CREATED)
        return Response(deserialized.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get():
        ...
    def put():
        ...
    def delete():
        ...