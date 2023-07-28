from django.shortcuts import render
from rest_framework import generics

from apps.post.models import Post, Tag, Category
from apps.post.serializers import PostSerializer, TagSerializer, CategorySerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer()
    queryset = Post.objects.all()


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer()
    queryset = Post.objects.all()


class PostRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer()
    queryset = Post.objects.all()


class PostDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PostSerializer()
    queryset = Post.objects.all()


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer()
    queryset = Post.objects.all()


class TagListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
