from django.urls import path

from .views import (
    PostAPIView, PostCategoriesAPIView, PostRetrieveAPIView,
    PostCategoryRetrieveAPIView
)


urlpatterns = [
    path('api/v1/posts/', PostAPIView.as_view()),
    path('api/v1/categories/', PostCategoriesAPIView.as_view()),
    path('api/v1/posts/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('api/v1/categories/<int:pk>/', PostCategoryRetrieveAPIView.as_view()),
]
