from django.urls import path
from .views import *



# Create your urls here.

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),

]
