from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth, User
from mysite.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Organisation, PlacementsOff, Student, Faculty
import random

# Create your views here.
def home(request):
    if request.session.has_key("username"):
        return redirect("Organizationdashboard")
    else:
        return render(request, "landingpage.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.get(email=email)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("user exists")
            request.session["username"] = email
            return redirect("Organizationdashboard")
        else:
            return HttpResponse("invalid user")
    else:
        if request.session.has_key("username"):
            return redirect("Organizationdashboard")
        else:
            return render(request, "login.html")


def RegistrationOrganization(request):
    if request.session.has_key("username"):
        return redirect("Organizationdashboard")
    else:
        return render(request, "RegistrationOrganization.html")


def RegistrationPO(request):
    if request.session.has_key("username"):
        return redirect("Organizationdashboard")
    else:
        return render(request, "RegistrationPO.html")


def RegistrationStudent(request):
    if request.session.has_key("username"):
        return redirect("Organizationdashboard")
    else:
        return render(request, "RegistrationStudent.html")


def RegistrationFaculty(request):
    if request.session.has_key("username"):
        return redirect("Organizationdashboard")
    else:
        return render(request, "RegistrationFaculty.html")


@login_required(login_url="login")
def contactus(request):
    return render(request, "contactus.html")


def send_otp(request, gmail):
    s = random.randint(111111, 999999)
    subject = "Email Verification"
    otp = str(s)
    message = "Thanks for choosing HYSEA. Your 6-digit verification code is" + otp + "."
    send_mail(subject, message, EMAIL_HOST_USER, [gmail], fail_silently=False)
    return JsonResponse({"otp": otp})


def registerOrg(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        auth.login(request, user)
        request.session["username"] = username
        x = Organisation.objects.create(organisation_name=username)
        x.save()
        return redirect("Organizationdashboard")


def registerPO(request):
    if request.method == "POST":
        username = request.POST["name"]
        mobile_num = request.POST["number"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        auth.login(request, user)
        request.session["username"] = username
        x = PlacementsOff.objects.create(clg_name=username, phn_no=mobile_num)
        x.save()
        return redirect("Organizationdashboard")


def registerStudent(request):
    if request.method == "POST":
        username = request.POST["name"]
        mobile_num = request.POST["number"]
        email = request.POST["email"]
        password = request.POST["password"]
        clg_name = request.POST["clg_name"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        auth.login(request, user)
        request.session["username"] = username
        x = Student.objects.create(
            student_name=username, clg_name=clg_name, phn_no=mobile_num
        )
        x.save()
        return redirect("Organizationdashboard")


def registerFaculty(request):
    if request.method == "POST":
        username = request.POST["name"]
        mobile_num = request.POST["number"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        auth.login(request, user)
        request.session["username"] = username
        x = Faculty.objects.create(faculty_name=username, phn_no=mobile_num)
        x.save()
        return redirect("Organizationdashboard")


@login_required(login_url="login")
def Organizationdashboard(request):
    return render(request, "Organizationdashboard.html")


@login_required(login_url="login")
def jobspost(request):
    return render(request, "jobspost.html")


@login_required(login_url="login")
def internshippost(request):
    return render(request, "internshippost.html")


@login_required(login_url="login")
def editresume(request):
    return render(request, "editresume.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return render(request, "landingpage.html")

