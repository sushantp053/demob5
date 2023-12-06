from django.shortcuts import render
from home.models import *

# Create your views here


def home(request):
    return render(request, "home.html")


def about(request):

    return render(request, "about.html")


def student(request):

    st = Student.objects.all()

    for s in st:
        print(s.roll, s.name, s.city)
    for s in st:
        if (s.roll != 2):
            print(s.name)

    return render(request=request, template_name="student.html", context={'stud': st})
