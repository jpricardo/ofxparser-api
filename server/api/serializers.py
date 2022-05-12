from django.contrib.auth.models import User, Group
from rest_framework import serializers
from server.api.convert import convert_file


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FileSerializer(serializers.Serializer):

    filename = serializers.CharField(required=True, max_length=100)
    base64content = serializers.CharField(required=True)
    format = serializers.CharField(required=True, max_length=10)

    def convert(self):
        return convert_file(self.instance)

    def __str__(self):
        return self.instance['filename']
