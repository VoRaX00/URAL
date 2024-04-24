from django.urls import path

from car_cargo import views

app_name = 'car_curgo'

urlpatterns = [
    path('addCargo/', views.addCargo, name='addCargo'),
    path('addCar/', views.addCar, name='addCar')
]