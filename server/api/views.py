from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from server.api.serializers import UserSerializer, GroupSerializer, FileSerializer

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def get_transactions(request):
    data = request.data
    file = FileSerializer(data).convert()
    return Response(file)
