from django.urls import path
from .views import employee_list, EmployeeAPIView, EmployeeDetailAPIView

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("api/employees/", EmployeeAPIView.as_view(), name="employee_api"),
    path("api/employees/<int:pk>/", EmployeeDetailAPIView.as_view(), name="employee_detail_api"),
]
