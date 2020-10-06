from django.contrib import admin
from django.urls import path
from designathon import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("send_otp", views.send_otp, name="send_otp"),
    path(
        "RegistrationOrganization",
        views.RegistrationOrganization,
        name="RegistrationOrganization",
    ),
    path("RegistrationPO", views.RegistrationPO, name="RegistrationPO"),
    path("RegistrationStudent", views.RegistrationStudent, name="RegistrationStudent"),
    path("RegistrationFaculty", views.RegistrationFaculty, name="RegistrationFaculty"),
    path("contactus", views.contactus, name="contactus"),
    path("registerOrg", views.registerOrg, name="registerOrg"),
    path(
        "Organizationdashboard",
        views.Organizationdashboard,
        name="Organizationdashboard",
    ),
    path("jobspost", views.jobspost, name="jobspost"),
    path("internshippost", views.internshippost, name="internshippost"),
    path("editresume", views.editresume, name="editresume"),
    path("logout", views.logout, name="logout"),
    path("registerPO",views.registerPO,name="registerPO"),
    path("registerStudent",views.registerStudent,name="registerStudent"),
    path("registerFaculty",views.registerFaculty,name="registerFaculty")
]

