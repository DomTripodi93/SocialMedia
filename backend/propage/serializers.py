from .models import Propage, ProUser, Posts
from rest_framework import serializers


class PropageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='propage-detail', read_only=True)
    class Meta:
        model = Propage
        fields = ('user', 'bio', 'interests', 'goals')

class ProUserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProUser
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = ProUser(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('user_id', 'title', 'body', 'created_at')
        extra_kwargs = {'user_id' : {'read_only': True}}