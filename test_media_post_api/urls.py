from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    PostList,
    PostDetail,
    CommentList,
    CommentDetail,
    DraftDetail,
    DraftList
)

urlpatterns = [
    path('api/posts', PostList.as_view()),
    path('api/post/<uuid:pk>', PostDetail.as_view()),
    path('api/comments', CommentList.as_view()),
    path('api/post/comment/<uuid:pk>', CommentDetail.as_view()),
    path('api/draft',DraftList.as_view()),
    path('api/draft/<uuid:pk>', DraftDetail.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]