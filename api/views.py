from django.http import JsonResponse
from django.shortcuts import render
from home.models import *
from rest_framework import viewsets
from api.serializers import *

# Create your views here.


def demoapi(request):
    student = Student.objects.all()

    return JsonResponse({"data": list(student.values("name", "roll", "city", "marks", "pass_year", "mobile", "email", "department_id"))})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


