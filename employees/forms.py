from django import forms
from django.forms import ModelForm
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


