from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)