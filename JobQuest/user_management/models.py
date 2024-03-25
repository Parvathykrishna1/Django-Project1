from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import JobListing

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer_recruiter', 'Employer/Recruiter'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

class ReportedIssue(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    description = models.TextField()
    resolved = models.BooleanField(default=False)
