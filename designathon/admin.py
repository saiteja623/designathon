from django.contrib import admin

# Register your models here.
from .models import (
    Student,
    StudentTopics,
    Organisation,
    OrganisationTopics,
    Faculty,
    PlacementsOff,
)

admin.site.register(Student)
admin.site.register(StudentTopics)
admin.site.register(Organisation)
admin.site.register(OrganisationTopics)
admin.site.register(PlacementsOff)
admin.site.register(Faculty)

