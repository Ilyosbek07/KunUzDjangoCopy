from django.urls import path

from apps.post.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    PostRetrieveAPIView,
    TagListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # POST API Urls
    path("", PostListAPIView.as_view()),
    path("", PostCreateAPIView.as_view()),
    path("<int:pk>/", PostRetrieveAPIView.as_view()),
    path("<int:pk>/", PostUpdateAPIView.as_view()),
    path("<int:pk>/", PostDestroyAPIView.as_view()),

    # TAG API Urls
    path("tag/", TagListCreateAPIView.as_view()),
    path("tag/<int:pk>/", TagRetrieveUpdateDestroyAPIView.as_view()),

    # CATEGORY API Urls
    path("category/", CategoryListCreateAPIView.as_view()),
    path("category/<int:pk>/", CategoryRetrieveUpdateDestroyAPIView.as_view()),

]
