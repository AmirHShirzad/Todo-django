from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('update_task/<str:pk>/', update_task, name='update_task'),


]
