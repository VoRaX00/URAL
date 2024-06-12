from django.urls import path

from car_cargo import views

app_name = 'car_curgo'

urlpatterns = [
    path('addCargo/', views.add_cargo, name='addCargo'),
    path('addCar/', views.add_car, name='addCar'),
    path('viewCargo/', views.view_cargo, name='viewCargo'),
    path('viewCar/', views.view_car, name='viewCar'),
    path('myCargo/', views.my_cargo, name='myCargo'),
    path('myCar/', views.my_car, name='myCar'),
    path('sendCargo/', views.send_notification_cargo, name='sendCargo'),
    path('sendCar/', views.send_notification_car, name='sendCar'),
]