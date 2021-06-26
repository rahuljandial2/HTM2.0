from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tasks/', views.TaskViewList.as_view(), name='tasks'),
    # # path('users/', views.TaskViewList.as_view()),
    # path('tasks/<int:id>/', views.TaskViewDetail.as_view(), name='task'),

    path('auth-token/', obtain_auth_token, name='get_token'),
    path('user-register/', views.ReqisterView.as_view(), name='register'),
]