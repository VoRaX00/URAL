from django.urls import path

from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='edit_profile')
]