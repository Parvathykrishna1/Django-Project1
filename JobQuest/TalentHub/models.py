from django.db import models

class RecruiterProfile(models.Model):
    user = models.OneToOneField('user_management.CustomUser', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(blank=True, null=True)
    company_location = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)

class JobListing(models.Model):
    employer = models.ForeignKey('user_management.CustomUser', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    required_qualifications = models.TextField()
    desired_qualifications = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    salary_range = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    company_benefits = models.TextField()
    how_to_apply = models.TextField()
    other_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title
