from django.db import models

class Department(models.Model):
  department_name = models.CharField(max_length=100)

  def __str__(self):
    return self.department_name

class Employee(models.Model):
  employee_name = models.CharField(max_length=70)
  department = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)
  date_of_joining = models.DateField()
  photo_file_name = models.FileField()

  def __str__(self):
    return self.employee_name
