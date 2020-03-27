from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('employee/?P<int:employee_id>/', views.employee, name="employee"),
    path('new_employee', views.new_employee, name="new_employee"),
    path('employee/delete?P<int:employee_id>/', views.delete_employee, name="delete"),
]


