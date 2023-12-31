from django.http import JsonResponse
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
        if next != None:
            return render(request, "login.html", {'next': next})
        else:
            return render(request, "login.html")

    if (request.method == "POST"):
        next = request.POST.get("next")
        username = request.POST.get("username")
        password = request.POST.get("password")
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


def demoapi(request):

    return JsonResponse({'message': 'Hello World', 'status': 200, 'data': {'name': 'Rahul', 'age': 20}})


def details(request, id):

    st = Student.objects.get(roll=id)
    print(st)

    return render(request, "studentdetails.html", {'stud': st})

def edit(request,id):
    st = Student.objects.get(roll=id)
    d = Department.objects.all()
    return render(request, "editstudent.html", {'stud': st, 'departments': d})


def update(request):
    roll = request.POST.get("roll")
    name = request.POST.get("name")
    city = request.POST.get("city")
    marks = request.POST.get("marks")
    pass_year = request.POST.get("passyear")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    department = request.POST.get("department")

    st = Student.objects.get(roll=roll)
    st.name = name
    st.city = city
    st.marks = marks
    st.pass_year = pass_year
    st.mobile = mobile
    st.email = email
    d = Department.objects.get(id=department)
    st.department = d
    st.save()
    return redirect("/details/"+str(roll))

def delete(request,id):
    st = Student.objects.get(roll=id)
    st.delete()
    return redirect("/student")