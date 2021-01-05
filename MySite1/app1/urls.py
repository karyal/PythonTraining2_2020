from django.urls import path
import app1.views as views

urlpatterns = [
    path('', views.index),
]