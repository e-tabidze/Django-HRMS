from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('employee/?P<int:employee_id>/', views.employee, name="employee")
]


