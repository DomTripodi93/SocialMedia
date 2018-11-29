from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from .models import Propage, ProUser, Posts
from .forms import UserCreationForm

def logout_view(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('login')
        else: return redirect('login')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)

def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Dominic\'s Showcase',
        'posts': posts
    }
    return render(request, 'layout/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post,
        'user': request.user
    }

    return render(request, 'posts/details.html', context)

class PostCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login' 
    model = Posts
    fields = ['title', 'body']
    template_name = 'posts/create.html'    
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

        

class PostUpdate(UpdateView):
    model = Posts
    fields = ['title', 'body']
    template_name = 'posts/update.html'
    success_url = '/'
    context_object_name='post'
    def get_user(self, request):
        context = {
            'user': request.user
            }
        user = context['user']
        return user
    def get_context_data(self, **kwargs):
        post = super().get_context_data(**kwargs)
        post['user'] = Posts.get_user
        return post
    


class PostDelete(DeleteView):
    model = Posts
    template_name = 'posts/delete.html'
    success_url = '/'
    context_object_name='post'
    def get_user(self, request):
        context = {
            'user': request.user
            }
        user = context['user']
        return user
    def get_context_data(self, **kwargs):
        post = super().get_context_data(**kwargs)
        post['user'] = Posts.get_user
        return post



class PropageUpdate(UpdateView):
    model = Propage
    fields = ['bio', 'interests', 'goals']
    template_name = 'propage/update.html'
    success_url = '/accounts/profile'
    def get_user(self, request):
        user = request.user  
        return user


def profile(request):
    posts = Posts.objects.filter(user_id= request.user.id)
    context = {
        'user': request.user,
        'posts': posts
    }

    return render(request, 'propage/profile.html', context)
