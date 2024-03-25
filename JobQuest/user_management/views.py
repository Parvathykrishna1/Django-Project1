from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from .forms import ResolveDisputeForm
from .models import ReportedIssue


def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'employer_recruiter':
                    return redirect('recruiter_home')
                else:
                    return redirect('job_seeker_home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dispute_list(request):
    disputes = ReportedIssue.objects.all()
    return render(request, 'dispute_list.html', {'disputes': disputes})

def resolve_dispute(request, dispute_id):
    dispute = get_object_or_404(ReportedIssue, pk=dispute_id)
    if request.method == 'POST':
        form = ResolveDisputeForm(request.POST)
        if form.is_valid():
            dispute.resolution = form.cleaned_data['resolution']
            dispute.resolved = True
            dispute.save()
            return redirect('dispute_list')
    else:
        form = ResolveDisputeForm()
    return render(request, 'resolve_dispute.html', {'form': form, 'dispute': dispute})
