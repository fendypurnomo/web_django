from django.contrib import admin
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  form = DepartmentForm

  list_filter = ('department_name',)
  search_fields = ('department_name',)
  ordering_fields = '__all__'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
  form = EmployeeForm

  list_display = ('employee_name', 'department', 'date_of_joining')
  list_filter = ('employee_name', 'department', 'date_of_joining')
  search_fields = ('employee_name', 'department__department_name')
  ordering_fields = '__all__'
