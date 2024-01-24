from django.contrib import messages
from django.shortcuts import render, redirect
from .models import JobApp
from .forms import JobAppForm
from django.db.models import Count

def job_application_list(request):
    applications = JobApp.objects.all()
    return render(request, 'job_app_tracker/job_application_list.html', {'applications': applications})

def statistics_view(request):
    applications_by_status = JobApp.objects.values('status').annotate(status_count=Count('status')).order_by('status')
    applications_by_company = JobApp.objects.values('company').annotate(company_count=Count('company')).order_by('company')

    status_data = {
        'labels': [app['status'] for app in applications_by_status],
        'data': [app['status_count'] for app in applications_by_status],
    }

    company_data = {
        'labels': [app['company'] for app in applications_by_company],
        'data': [app['company_count'] for app in applications_by_company],
    }

    context = {
        'applications_by_status': status_data, 
        'applications_by_company': company_data
    }

    return render(request, 'job_app_tracker/statistics.html', context)


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
