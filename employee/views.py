from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


def employee_list(request):
    qs = Employee.objects.values_list()
    return JsonResponse({"employees": list(qs)})


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return JsonResponse({"employees": serializer.data})
    
    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"employee": serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)


class EmployeeDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            return JsonResponse({"employee": serializer.data})
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"employee": serializer.data})
            return JsonResponse(serializer.errors, status=400)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return JsonResponse({"message": "Employee deleted successfully"}, status=204)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)