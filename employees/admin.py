from django.contrib import admin
from . models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position', 'date_of_employment', 'salary', 'working_history',
                    'employment_position', 'day_offs')


admin.site.register(Employee, EmployeeAdmin)
