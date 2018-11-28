from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from rest_framework import viewsets
from .serializers import PostsSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-created_at')
    serializer_class = PostsSerializer

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
    fields = ['title', 'body', 'created_at']
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


class PostDelete(DeleteView):
    model = Posts
    template_name = 'posts/delete.html'
    success_url = '/'