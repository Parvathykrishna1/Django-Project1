from django.urls import path
from . import views

urlpatterns = [
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('recruiter_profile/', views.recruiter_profile_view, name='recruiter_profile'),
    path('post_job/', views.post_job, name='post_job'),
    path('job_listing_detail/', views.job_listing_detail, name='job_listing_detail'),
    path('edit_job/<int:pk>/', views.edit_job, name='edit_job'),
    path('delete_job/<int:pk>/', views.delete_job, name='delete_job'),
    path('received_applications/',views.received_job_application_list, name ='received_applications'),
    path('process_application/<int:application_id>/', views.process_job_application, name='process_job_application'),
]
