from django.contrib import admin
from django.urls import path
from app1_1 import views

urlpatterns = [
    path('', views.index),
    path('f1/', views.f1),
]