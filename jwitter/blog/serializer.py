from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    text = serializers.CharField(max_length=1024)

    def validate_title(self, value):
        if value == "jaan":
            raise serializers.ValidationError(detail = {"text": "this text is not allowed."})
        return value

    def validate_title(self, value):
        return value.lower()

    def validate(self, value):
        title = value["title"]
        text = value["text"]
        if title.lower() == text.lower():
            raise serializers.ValidationError(detail={"title and text":"title and text cn not not be the same"})
        return value        

    def create(self, validated_data):
        return Post.objects.create(**validated_data)