from django.contrib import admin
from CareerForge.models import JobSeekerProfile, JobApplication
from .models import CustomUser, Issue

# Register your models here.
admin.site.register(JobSeekerProfile)
admin.site.register(JobApplication)
