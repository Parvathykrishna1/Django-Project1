from django.db import models
from user_management.models import CustomUser
from TalentHub.models import JobListing

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    job_listing = models.ForeignKey('TalentHub.JobListing', on_delete=models.CASCADE)
    applicant_name = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.applicant_profile.full_name}'s Application for {self.job_listing.job_title}"

class Issue(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    description = models.TextField()
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='open')

    def __str__(self):
        return f"Issue reported by {self.reported_by.username} - {self.job_listing}"