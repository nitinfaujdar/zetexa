from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/', TaskCreateView.as_view(), name='tasks-create'),
]