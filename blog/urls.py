from django.urls import path
from .views import *


# Create your urls here.

urlpatterns = [
    path('', index, name='blog-home'),
    path('about/', about, name='blog-about'),

]
