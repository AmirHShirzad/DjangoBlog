from django.shortcuts import render
from .models import Post


# Create your views here.


def index(request):
    # we use context to add data to our template
    context = {'posts': Post.objects.all()}

    return render(request, 'blog/index.html', context=context)


def about(request):
    # we send title from context to template to made some changes in title in tab of each page
    return render(request, 'blog/about.html', {'title': 'About'})
