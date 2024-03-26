from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from CareerForge.models import Issue
from .forms import LoginForm, RegistrationForm
from django.core.mail import send_mail
from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            subject = 'Welcome to JobQuest!'
            message = 'Thank you for registering with us. Your account has been created successfully.'
            from_email = 'jobquest@gmail.com'
            to_email = form.cleaned_data['email']

            send_mail(subject, message, from_email, [to_email], fail_silently=False)

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

def change_issues(request):
    issues = Issue.objects.all()
    return render(request, 'issue_chnage_list.html', {'issues': issues})