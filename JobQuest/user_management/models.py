# user_management/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer_recruiter', 'Employer/Recruiter'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

