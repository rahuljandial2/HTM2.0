from django.shortcuts import render

# Create your views here.
from django import urls
from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task


class HomeView(APIView):
    
    def get(self, request):
        links = {
            # f'{urls.reverse("tasks")}' : 'all-user-tasks',
            # f'{urls.reverse("tasks")}<int>/' : 'particular-task',
            f'{urls.reverse("get_token")}' : 'login',
            # f'{urls.reverse("register")}' : 'signup',
        }

        return Response(links)


