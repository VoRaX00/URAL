from django.urls import path

from car_cargo import views

app_name = 'car_curgo'

urlpatterns = [
    path('addCargo/', views.addCargo, name='addCargo'),
    path('addCar/', views.addCar, name='addCar'),
    path('viewCargo/',views.viewCargo, name='viewCargo'),
    path('viewCar/', views.viewCar, name='viewCar'),
    path('myCargo/', views.myCargo, name='myCargo'),
    path('myCar/', views.myCar, name='myCar'),
    path('sendCargo/', views.send_notification_cargo, name='sendCargo'),
    path('sendCar/', views.send_notification_car, name='sendCar'),
]