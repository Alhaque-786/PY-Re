# blog/urls.py
from django.urls import path
from .views import PostList, PostDetail, UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
