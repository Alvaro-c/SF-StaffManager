from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id",
                  "name",
                  "surname",
                  "email",
                  "manager",
                  "is_active",
                  "is_manager"
                  )



