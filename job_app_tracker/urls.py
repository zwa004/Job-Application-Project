from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.job_application_list, name='job_application_list'),
    path('applications/new/', views.create_job_application, name='create_job_application'),
    path('applications/<int:pk>/edit/', views.edit_job_application, name='edit_job_application'),
    path('applications/<int:pk>/delete/', views.delete_job_application, name='delete_job_application'),
    path('statistics/', views.statistics_view, name='statistics_view'),
    path('applications/delete_all/', views.delete_all_job_applications, name='delete_all_job_applications'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)