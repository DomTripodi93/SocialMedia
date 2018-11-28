from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout
from . import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/profile/', include('propage.urls')),
    path('accounts/register', views.register, name='register'),
    path('accounts/logout/', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls'))
] 
