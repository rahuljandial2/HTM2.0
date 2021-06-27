from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import apis


urlpatterns = [
    path('', apis.HomeView.as_view(), name='home'),
    path('tasks/', apis.TaskViewList.as_view(), name='tasks'),
    path('tasks/<int:id>/', apis.TaskViewDetail.as_view(), name='task'),
    path('user-details/', apis.UserDetailView.as_view(), name='all-users'),
    path('auth-token/', obtain_auth_token, name='get_token'),
    path('user-register/', apis.ReqisterView.as_view(), name='register'),
]