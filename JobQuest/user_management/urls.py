from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('issue_change_list/', views.change_issues, name='issue_change_list'),

]