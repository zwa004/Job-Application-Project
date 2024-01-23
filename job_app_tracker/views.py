from django.contrib import messages
from django.shortcuts import render, redirect
from .models import JobApp
from .forms import JobAppForm

def job_application_list(request):
    applications = JobApp.objects.all()
    return render(request, 'job_app_tracker/job_application_list.html', {'applications': applications})

def home(request):
    return render(request, 'home.html')

def delete_job_application(request, pk):
    application = JobApp.objects.get(id=pk)
    application.delete()
    return redirect('job_application_list')

def create_job_application(request):
    if request.method == 'POST':
        form = JobAppForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application successfully submitted.')
            return redirect('job_application_list')
        else:
            messages.error(request, 'Application submission failed.')
    else:
        form = JobAppForm()

    return render(request, 'job_app_tracker/create_job_application.html', {'form': form})

def edit_job_application(request, pk):
    application = JobApp.objects.get(pk=pk)
    if request.method == "POST":
        form = JobAppForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_application_list')
    else:
        form = JobAppForm(instance=application)
    return render(request, 'job_app_tracker/edit_job_application.html', {'form': form})
