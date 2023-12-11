from django.shortcuts import render, redirect, HttpResponse
from home.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here

def index(request):
    return render(request, "index.html")

@login_required
def home(request):
    return render(request, "home.html")


@login_required
def about(request):

    return render(request, "about.html")


@login_required
def student(request):

    st = Student.objects.all()

    for s in st:
        print(s.roll, s.name, s.city)
    for s in st:
        if (s.roll != 2):
            print(s.name)

    return render(request=request, template_name="student.html", context={'stud': st})


@login_required
def addStudent(request):

    d = Department.objects.all()
    return render(request, "addstudent.html", {'departments': d})


@login_required
def addStud(request):

    name = request.POST.get("name")
    roll = request.POST.get("roll")
    city = request.POST.get("city")
    marks = request.POST.get("marks")
    pass_year = request.POST.get("passyear")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    department = request.POST.get("department")

    st = Student(name=name, roll=roll, city=city, marks=marks,
                 pass_year=pass_year, mobile=mobile, email=email, department_id=department)
    st.save()
    s = Student.objects.all()
    return render(request, "student.html", {'stud': s})


def logoutUser(request):
    logout(request)
    return redirect("/login")


def loginUser(request):

    if (request.method == "GET"):
        next = request.GET.get("next")
        print(next)
        if next != None:
            return render(request, "login.html", {'next': next})
        else:
            return render(request, "login.html")

    if (request.method == "POST"):
        next = request.POST.get("next")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            # return HttpResponse("<h1> Login Success </h1>")
            if next != None:
                return redirect(next)
            return redirect("/home")

        else:
            message = "Invalid Username or Password"
            return render(request, "login.html", {'message': message})

    return render(request, "login.html")
