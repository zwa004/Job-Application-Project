from django.shortcuts import render
from .models import JobApp

def job_application_list(request):
    applications = JobApp.objects.all()
    return render(request, 'job_app_tracker/job_application_list.html', {'applications': applications})

def home(request):
    return render(request, 'home.html')
