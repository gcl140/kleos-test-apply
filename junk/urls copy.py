from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', views.logout, name='logout'),
    path('assignments/', views.assignments_view, name='assignments'),
    path('students/', views.students, name='students'),
    path('exams/', views.exams_view, name='exams'),
    path('notes/', views.notes_view, name='notes'),
    path('resources/', views.resources_view, name='resources'),
    path('counsellor_dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]
