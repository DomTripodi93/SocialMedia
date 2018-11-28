from .models import Propage
from rest_framework import serializers


class PropageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='propage-detail', read_only=True)
    class Meta:
        model = Propage
        fields = ('user', 'bio', 'interests', 'goals')

