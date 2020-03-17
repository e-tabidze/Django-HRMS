from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


def index(request):
    employees = Employee.objects.all()
    for employee in employees:
        employee.salary *= 0.8
    return render(request, 'index.html', {'employees': employees})


def employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    context = {
        'employee': employee,
    }
    return render(request, 'employee.html', context=context)
