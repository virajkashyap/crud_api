from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("",index),
    path('api/users',usersListView),
    path('api/users/<int:pk>',userListView),

    
    
]