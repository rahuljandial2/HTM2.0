from django.shortcuts import render

# Create your views here.
from django import urls
from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import UserSerializer


class HomeView(APIView):
    
    def get(self, request):
        links = {
            # f'{urls.reverse("tasks")}' : 'all-user-tasks',
            # f'{urls.reverse("tasks")}<int>/' : 'particular-task',
            f'{urls.reverse("get_token")[5:]}' : 'login',
            f'{urls.reverse("register")[5:]}' : 'signup',
        }

        return Response(links)




class ReqisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)


