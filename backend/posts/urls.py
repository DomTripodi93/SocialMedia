from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', views.PostsViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('details/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'), 
    path('details/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'), 
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]