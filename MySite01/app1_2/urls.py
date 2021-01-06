from django.urls import path
import app1_2.views as views

urlpatterns = [
    path('', views.index),
]