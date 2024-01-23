from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.job_application_list, name='job_application_list'),
    path('applications/new/', views.create_job_application, name='create_job_application'),
    path('applications/<int:pk>/edit/', views.edit_job_application, name='edit_job_application'),
    path('applications/<int:pk>/delete/', views.delete_job_application, name='delete_job_application'),
    # do not include 'job_app_tracker.urls' or 'settings_and_config.urls' here, as it would cause a circular include
]