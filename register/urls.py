from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('register/', views.register, name="register")
]

