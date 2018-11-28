from django.shortcuts import render
from ..models import Propage
from rest_framework import viewsets
from .serializers import PropageSerializer

class PropageViewSet(viewsets.ModelViewSet):
    queryset = Propage.objects.all().order_by('-date_joined')
    serializer_class = PropageSerializer