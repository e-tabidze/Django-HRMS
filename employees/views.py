from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import EmployeeFilter
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


def index(request):
    employees = Employee.objects.all()
    for employee in employees:
        employee.salary *= 0.8

    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    context = {
        'myFilter': myFilter,
        'employees': employees
    }
    return render(request, 'index.html', context)


def employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = PostForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['working_history ']
    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee.html', context=context)


def new_employee(response):
    new_employee = Employee.objects.all()
    form = EmployeeForm()
    context = {}
    if response.method == "POST":
        form = EmployeeForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
        return redirect("/employees/")
    else:
        form = EmployeeForm()
    context = {
        'employee': employee,
        'form': form
    }
    return render(response, 'new_employee.html', context)


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm()
    if request.method == "POST":
        employee.delete()
        return redirect('/employees/')
    context = {'employee': employee}
    return render(request, 'delete.html', context)
