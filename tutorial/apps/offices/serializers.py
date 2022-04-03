from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'department_name')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'department', 'date_of_joining')
