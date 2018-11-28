from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))

def index(request):
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Dominic\'s Showcase',
        'posts': posts
    }

    return render(request, 'layout/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else: return redirect('login')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)