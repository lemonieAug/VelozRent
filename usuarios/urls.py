from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    #path('profile/', views.profile, name='profile'),
    #path('update_profile/', views.update_profile, name='update_profile'),
    #path('change_password/', auth_views.PasswordChangeView.as_view(template_name='usuarios/change_password.html'), name='change_password'),
    #path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
]