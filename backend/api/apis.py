from django.shortcuts import render

# Create your views here.
from django import urls
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Profile, Task
from .serializers import UserDetailSerializer, UserSerializer, TaskSerializer
from .permissions import IsOwner



class HomeView(APIView):
    
    def get(self, request):
        links = {
            f'{urls.reverse("tasks")[5:]}' : 'all-user-tasks',
            f'{urls.reverse("tasks")[5:]}<int>/' : 'particular-task',
            f'{urls.reverse("all-users")[5:]}/' : 'all-users',
            f'{urls.reverse("get_token")[5:]}' : 'login',
            f'{urls.reverse("register")[5:]}' : 'signup',
        }

        return Response(links)


class TaskViewList(APIView):
    permission_classes = [IsOwner]

    def get_user(self, request):
        return request.user

    def get(self, request):
        queryset    = get_list_or_404(Task, user=request.user)
        serializer  = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = TaskSerializer(data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskViewDetail(APIView):
    permission_classes = [IsOwner]

    def get_object(self, id, user):
        return get_object_or_404(Task, id=id, user=user)

    def get(self, request, id):
        task        = self.get_object(id, request.user)
        serializer  = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task        = self.get_object(id, request.user)
        serializer  = TaskSerializer(task, data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        task    = self.get_object(id)
        task.delete()
        return Response(data={'messege': f'object sucessfully deleted'}, status=204)


class  UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(seld, request):
        user        = request.user
        serializer  = UserDetailSerializer(user)
        return Response(serializer.data)

class ReqisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)


