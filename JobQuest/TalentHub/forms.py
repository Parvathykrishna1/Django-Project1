from django import forms
from .models import RecruiterProfile, JobListing

class RecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ['full_name', 'designation', 'company_name', 'company_description', 'company_location', 'industry', 'established_year']


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ['employer']