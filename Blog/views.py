from django.shortcuts import render
from .models import Post


# Create your views here.

posts = [

    {'author': 'Amir',
        'title': 'first post',
        'created_date': '4 september',
        'content': 'This is my first post.'},

    {'author': 'Reza',
        'title': 'seconed post',
        'created_date': '5 september',
        'content': 'I posted a content.'}



]


def index(request):
    # we use context to add data to our template
    context = {'posts': Post.objects.all()}

    return render(request, 'blog/index.html', context=context)


def about(request):
    # we send title from context to template to made some changes in title in tab of each page
    return render(request, 'blog/about.html', {'title': 'About'})
