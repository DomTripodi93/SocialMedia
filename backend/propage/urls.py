from . import views

from rest_framework import routers

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout


router = routers.DefaultRouter()
router.register('profile', views.ProUserViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('propage', views.PropageViewSet)
router.register('posts', views.PostsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='pro_api')),
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



"""
    path('accounts/login/', views.login_view),
def login_view(request):
    login(request)
    return render(request, 'registration/login.html', context) 
"""