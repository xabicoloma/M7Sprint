from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('register/', views.registro, name='register'),
]