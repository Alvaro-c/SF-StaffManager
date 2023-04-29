from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from employees.models import Employee
from employees.serializers import EmployeeSerializer


# View for CRUD over Employees (Views are like Controllers in Spring, for example)
class EmployeeAPIView(APIView):
    def get(self, request, employee_id=None):
        if employee_id:
            # I actually don't use the get by ID, but I prefer to have it ready
            employee = Employee.objects.filter(id=employee_id).first()
            if employee:
                response = EmployeeSerializer(employee)
                return Response(response.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        employees = Employee.objects.all()
        response = EmployeeSerializer(employees, many=True)
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        if employee:
            employee.name = request.data.get("name")
            employee.surname = request.data.get("surname")
            employee.email = request.data.get("email")
            manager_id = request.data.get("manager")
            manager = Employee.objects.filter(id=manager_id).first()
            # If there is no manager, a 0 is sent by the frontend
            # This condition checks that and assign None, or the correct manager
            employee.manager = None
            if manager != 0:
                employee.manager = manager

            employee.is_active = request.data.get("is_active")
            employee.is_manager = request.data.get("is_manager")
            employee.save()

            response = EmployeeSerializer(employee)
            return Response(response.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        employee.delete()
        return Response({}, status=status.HTTP_200_OK)
