from django.shortcuts import render, redirect, get_object_or_404
from TalentHub.forms import RecruiterProfileForm, JobListingForm
from TalentHub.models import RecruiterProfile, JobListing
from django.contrib import messages
from CareerForge.models import JobApplication
from django.contrib.auth.decorators import login_required

def recruiter_home(request):
    return render(request, 'recruiter_home.html')

@login_required
def recruiter_profile_view(request):
    if request.user.user_type == 'employer_recruiter':
        try:
            profile = request.user.recruiterprofile
        except RecruiterProfile.DoesNotExist:
            profile = RecruiterProfile(user=request.user)

        if request.method == 'POST':
            form = RecruiterProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('recruiter_home')
        else:
            form = RecruiterProfileForm(instance=profile)
        return render(request, 'recruiter_profile.html', {'form': form})
    else:
        return redirect('login')


def post_job(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.employer = request.user
            job_listing.save()

            return redirect('job_listing_detail')
    else:
        form = JobListingForm()
    return render(request, 'post_job.html', {'form': form})

def job_listing_detail(request):
    job_listings = JobListing.objects.all()
    return render(request, 'job_listing_detail.html', {'job_listings': job_listings})


def edit_job(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk, employer=request.user)
    if request.method == 'POST':
        form = JobListingForm(request.POST, instance=job_listing)
        if form.is_valid():
            form.save()
            return redirect('job_listing_detail')
    else:
        form = JobListingForm(instance=job_listing)
    return render(request, 'edit_job.html', {'form': form})

def delete_job(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk, employer=request.user)
    if request.method == 'POST':
        job_listing.delete()
        return redirect('recruiter_home')
    return render(request, 'confirm_delete_job.html', {'job_listing': job_listing})

def received_job_application_list(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'received_application_list.html', {'job_applications': job_applications})

def process_job_application(request, application_id):
    job_application = get_object_or_404(JobApplication, id=application_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        if new_status in ['approved', 'rejected']:
            job_application.status = new_status
            job_application.save()
            messages.success(request, f'Job application status updated to {new_status.capitalize()} successfully.')
            return redirect('recruiter_home')
        else:
            messages.error(request, 'Invalid status provided.')
            return redirect('job_apply_status')

    return render(request, 'process_job_application.html', {'job_application': job_application})