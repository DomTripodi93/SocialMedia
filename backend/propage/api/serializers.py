from ..models import Propage
from rest_framework import serializers


class PropageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propage
        fields = ('user', 'bio', 'interests', 'goals')
