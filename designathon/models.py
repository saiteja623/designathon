from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=225, default="")
    clg_name = models.CharField(max_length=225)
    phn_no = models.BigIntegerField()


class StudentTopics(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=225)


class PlacementsOff(models.Model):
    clg_name = models.CharField(max_length=225)
    phn_no = models.BigIntegerField()


class Organisation(models.Model):
    organisation_name = models.CharField(max_length=225)


class OrganisationTopics(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    topic = models.CharField(max_length=225, default="")


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=225)
    phn_no = models.BigIntegerField()

