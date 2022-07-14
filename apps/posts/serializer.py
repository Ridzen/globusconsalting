from rest_framework import serializers

from apps.posts.models import Post, PostCategories


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'tag', 'created_at', 'is_active', 'updated_at')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class PostCategorySerializer(serializers.ModelSerializer):
    products = PostSerializer(many=True)

    class Meta:
        model = PostCategories
        fields = "__all__"