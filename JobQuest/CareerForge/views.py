from django.shortcuts import render, redirect, get_object_or_404
from CareerForge.forms import JobSeekerProfileForm,JobApplicationForm, JobSearchForm
from CareerForge.models import JobSeekerProfile, JobApplication
from TalentHub.models import JobListing
from django.db.models import Q
from django.contrib import messages
from .forms import IssueForm
from django.contrib.auth.decorators import login_required
from CareerForge.models import Issue


def job_seeker_home(request):
    if request.user.is_authenticated and not request.user.user_type == 'employer_recruiter':
        return render(request, 'job_seeker_home.html')
    else:
        return redirect('login')

def create_or_update_profile(request):
    try:
        profile = request.user.jobseekerprofile
    except JobSeekerProfile.DoesNotExist:
        profile = JobSeekerProfile(user=request.user)

    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('job_seeker_home')
    else:
        form = JobSeekerProfileForm(instance=profile)
        return render(request, 'job_seeker_profile.html', {'form': form})


def job_openings_view(request):
    job_listings = JobListing.objects.select_related('employer__recruiterprofile').all()
    return render(request, 'job_listing_list.html', {'job_listings': job_listings})

def job_search(request):
    query = request.GET.get('q')
    job_listings = JobListing.objects.filter(
        Q(job_title__icontains=query) |
        Q(job_description__icontains=query)
    ) if query else JobListing.objects.all()
    return render(request, 'job_search.html', {'job_listings': job_listings})


def apply_job(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job_listing = job_listing
            job_application.save()
            return redirect('job_apply_status')
    else:
        form = JobApplicationForm()

    return render(request, 'apply_job.html', {'job_listing': job_listing, 'form': form})

def job_apply_status(request):
    return render(request,'job_apply_status.html')

def job_application_list(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'job_applications.html', {'job_applications': job_applications})

def job_search_filter_view(request):
    if request.method == 'GET':
        form = JobSearchForm(request.GET)
        if form.is_valid():
            keywords = form.cleaned_data.get('keywords')
            location = form.cleaned_data.get('location')
            industry = form.cleaned_data.get('industry')

            job_listings = JobListing.objects.all()
            if keywords:
                job_listings = job_listings.filter(title__icontains=keywords)
            if location:
                job_listings = job_listings.filter(location__icontains=location)
            if industry:
                job_listings = job_listings.filter(industry__icontains=industry)

            return render(request, 'job_search_results.html', {'job_listings': job_listings})
    else:
        form = JobSearchForm()

    return render(request, 'job_seeker_home.html', {'form': form})


def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            try:
                issue = form.save(commit=False)
                issue.reported_by = request.user
                issue.save()
                messages.success(request, 'Issue reported successfully!')
                return redirect('job_seeker_home')
            except Exception as e:
                messages.error(request, f'An error occurred while saving the issue: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors.')
    else:
        form = IssueForm()
    return render(request, 'report_issue.html', {'form': form})

