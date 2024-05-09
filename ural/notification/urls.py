from django.urls import path

from notification import views

app_name = 'notification'

urlpatterns = [
    path('notification/', views.allNotification, name='notify'),
    path('viewCargo/', views.send_notification_cargo, name='sendCargo'),
    path('viewCar/', views.send_notification_car, name='sendCar'),
]
