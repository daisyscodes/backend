from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     if self.request.method == 'PUT':
    #         return [permissions.IsAuthenticated(), IsAccountOwner(), ]
    #
    #     if self.request.method == 'POST':
    #         return [permissions.AllowAny()]
    #
    #     if self.request.method == 'DELETE':
    #         return [permissions.IsAuthenticated(), IsAccountOwner(), ]
    #
    #     if self.request.method == 'GET':
    #         return [permissions.IsAuthenticated()]
