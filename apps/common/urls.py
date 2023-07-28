from django.urls import path

from apps.common.views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    FAQListCreateAPIView,
    FAQRetrieveUpdateDestroyAPIView,
    ContactListCreateAPIView,
    ContactRetrieveUpdateDestroyAPIView
)
urlpatterns = [
    path("user/", UserListCreateAPIView.as_view()),
    path("user/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view()),

    path("faq/", FAQListCreateAPIView.as_view()),
    path("faq/<int:pk>/", FAQRetrieveUpdateDestroyAPIView.as_view()),

    path("contact/", ContactListCreateAPIView.as_view()),
    path("contact/<int:pk>/", ContactRetrieveUpdateDestroyAPIView.as_view()),

]
