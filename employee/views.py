from django.shortcuts import render
from django.http import JsonResponse

from .models import Employee
# Create your views here.

def employee_list(request):
    qs = Employee.objects.values_list()
    return JsonResponse({"employees": list(qs)})
