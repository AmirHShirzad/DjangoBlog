from django.shortcuts import render, redirect
from .forms import UsersForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            # convert the information that users entered in to suitable format with cleaned_data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thanks {username} for signing up :)')
            return redirect('blog-home')
    else:
        form = UsersForm()

    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})
