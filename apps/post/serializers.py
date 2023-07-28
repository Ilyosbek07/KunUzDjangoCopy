from rest_framework import serializers

from apps.post.models import (
    Post,
    Category,
    Tag,
)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'sub_title',
            'category',
            'tag',
            'view_count',
            'slug',
            'description',
            'image'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )
