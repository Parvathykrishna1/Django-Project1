from django import forms
from .models import JobSeekerProfile,JobApplication

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ['full_name', 'title', 'bio', 'skills', 'education', 'work_experience', 'resume', 'phone_number', 'address', 'state', 'district']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_listing', 'applicant_name', 'resume', 'cover_letter']

class JobSearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    location = forms.CharField(required=False)
    industry = forms.CharField(required=False)

