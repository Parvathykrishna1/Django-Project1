from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('dispute_list/', views.dispute_list, name='dispute_list'),
    path('resolve_dispute/<int:dispute_id>/', views.resolve_dispute, name='resolve_dispute'),
]