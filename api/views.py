from django.http import JsonResponse
from django.shortcuts import render
from home.models import *

# Create your views here.


def demoapi(request):
    student = Student.objects.all()

    return JsonResponse({"data": list(student.values("name", "roll", "city", "marks", "pass_year", "mobile", "email", "department_id"))})
