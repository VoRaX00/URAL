from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path('registration/', views.registration, name='registration'),
    # path('profile/', views.profile, name='profile'),
]