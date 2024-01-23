from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.job_application_list, name='job_application_list'),
    # do not include 'job_app_tracker.urls' or 'settings_and_config.urls' here, as it would cause a circular include
]