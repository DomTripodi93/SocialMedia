from . import views

from django.urls import path, include
from django.conf import settings
from django.contrib.auth import login, logout


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('accounts/profile/', views.profile, name= 'propage'),
    path('accounts/profile/<slug:pk>/update/', views.PropageUpdate.as_view(), name='propage_update'), 
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/details/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'), 
    path('posts/details/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'), 
    path('posts/details/<int:id>/', views.details, name='details'),
    path('accounts/register', views.register, name='register'),
    path('accounts/logout/', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls'))
] 

