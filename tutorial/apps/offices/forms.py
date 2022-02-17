from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Department, Employee

class DepartmentForm(ModelForm):
  class Meta:
    model = Department
    fields = ('department_name',)
    labels = {
      'department_name': _('Department Name'),
    }

class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    fields = ('employee_name', 'department', 'date_of_joining', 'photo_file_name')
    labels = {
      'employee_name': _('Employee Name'),
      'department': _('Department Name'),
      'date_of_joining': _('Date of Joining'),
      'photo_file_name': _('Photo Profile')
    }
