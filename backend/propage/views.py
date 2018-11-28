from django.shortcuts import render
from django.http import HttpResponse
from .models import Propage
from django.contrib.auth.models import User
from posts.models import Posts
from rest_framework import viewsets, generics
from .serializers import PropageSerializer
from django.views.generic.edit import UpdateView

class PropageViewSet(viewsets.ModelViewSet):
    queryset = Propage.objects.all().order_by('-user')
    serializer_class = PropageSerializer


class PropageUpdate(UpdateView):
    model = Propage
    fields = ['bio', 'interests', 'goals']
    template_name = 'propage/update.html'
    success_url = '/accounts/profile'
    def get_user(self, request):
        context = {
            'user': request.user
            }
        return context
    user = 'context.user'

def profile(request):

    posts = Posts.objects.filter(user_id= request.user.username)

    context = {
        'user': request.user,
        'posts': posts
    }

    return render(request, 'propage/profile.html', context)
