from django.contrib import admin
from django.urls import path, include

from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(
        f"employee/",
        view=views.EmployeeAPIView.as_view(),
        name="get_employees",
    ),
    path(
        f"employee/<employee_id>/",
        view=views.EmployeeAPIView.as_view(),
        name="get_employee",
    ),
]
