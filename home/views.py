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


def addStudent(request):

    return render(request, "addstudent.html")


def addStud(request):

    name = request.POST.get("name")
    roll = request.POST.get("roll")
    city = request.POST.get("city")
    marks = request.POST.get("marks")
    pass_year = request.POST.get("passyear")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")

    st = Student(name=name, roll=roll, city=city, marks=marks,
                 pass_year=pass_year, mobile=mobile, email=email)
    st.save()
    s = Student.objects.all()
    return render(request, "student.html", {'stud': s})
