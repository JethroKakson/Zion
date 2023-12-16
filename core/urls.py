from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, UserPostListView, QuoteDetailView, QuoteListView, QuoteCreateView, Videos, VideoCreateView)

urlpatterns = [
    path('', views.home, name='home'),
    # path('memorize/', views.memorize, name='memorize'),
    path('tests/', views.tests, name='tests'),
    path('test/<int:test_id>/', views.questions, name='questions'),
    path('test-<int:test_id>/qtn-<int:pk>/answer/', views.answers, name='answers'),
    path('test-<int:test_id>/qtn-<int:qtn_id>/answer/', views.next_qtn, name='next_qtn'),
    path('study_tool/', views.study_tool, name='study_tool'),
    path('posts/', PostListView.as_view(), name='daily_missions'),
    path('quotes/', QuoteListView.as_view(), name='quotes'),
    path('videos/', Videos.as_view(), name='grad_vids'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('quote/new/', QuoteCreateView.as_view(), name='quote-create'),
    path('video/new/', VideoCreateView.as_view(), name='video-create'),
]