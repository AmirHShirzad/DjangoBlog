from django.urls import path
from .views import *
from users.views import register

# Create your urls here.

urlpatterns = [
    path('', index, name='blog-home'),
    path('about/', about, name='blog-about'),
    path('register/', register, name='users-register'),
]
