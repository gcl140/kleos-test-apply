from django.urls import path
from . import views


urlpatterns = [
    # path('register/', views.register, name='register'),
    path('register/<str:user_type>/', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', views.logout, name='logout'),
]
