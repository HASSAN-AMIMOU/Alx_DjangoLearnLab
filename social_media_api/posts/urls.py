from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import LikePostView, UnlikePostView, PostViewSet, CommentViewSet, FeedViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='user_feed'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]