from django.contrib import admin
from django.urls import path
from app2_1 import views

urlpatterns = [
    path('', views.index),
    path('get_message/', views.get_message),
]