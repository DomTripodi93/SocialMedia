from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'propage', views.PropageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", views.profile, name= 'propage'),
    path('<slug:pk>/update/', views.PropageUpdate.as_view(), name='propage_update'), 
]