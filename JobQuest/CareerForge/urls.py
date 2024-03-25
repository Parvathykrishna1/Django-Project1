from django.urls import path
from . import views

urlpatterns = [
    path('job_seeker_home/', views.job_seeker_home, name='job_seeker_home'),
    path('create_or_update_profile/', views.create_or_update_profile, name='create_or_update_profile'),
    path('job_listing_list/', views.job_openings_view, name='job_listing_list'),
    path('job_search/', views.job_search, name='job_search'),
    path('apply_job/<int:pk>/', views.apply_job, name='apply_job'),
    path('job_apply_status/', views.job_apply_status, name='job_apply_status'),
    path('job_applications/', views.job_application_list, name='job_applications'),
    path('searchjob/', views.job_search_filter_view, name='searchjob'),
]
