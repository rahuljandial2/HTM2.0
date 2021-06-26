from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Task

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        return(
            user == obj.user
        )

    def has_permission(self, request, view):
        user = request.user

        return(
            user.is_authenticated 
        )
