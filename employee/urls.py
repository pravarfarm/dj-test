from django.urls import path
from .views import employee_list, EmployeeAPIView, EmployeeDetailAPIView

urlpatterns = [
    path("employees/search/", EmployeeAPIView.as_view(), name="employee_api"),
    path("employees/search/<int:pk>/", EmployeeDetailAPIView.as_view(), name="employee_detail_api"),
]
