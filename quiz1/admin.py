from django.contrib import admin

from .models import PersonalInformation, Project


admin.site.register(Project)
admin.site.register(PersonalInformation)
