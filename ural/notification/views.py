from django.shortcuts import render
from .models import notifyCargo, notifyCar
from car_cargo.models import Cargo, Car
# Create your views here.
def allNotification(request):
    return render(request, 'notification.html')

def send_notification_cargo(request):
    print("send")
    if request.POST:
        cargo = Cargo.objects.get(id=request.POST['cargo_id'])
        if request.user == cargo.user_id:
            return render(request, 'viewCargo.html')
        notify = notifyCargo(cargo=cargo, first_user=request.user, second_user=cargo.user_id)
        notify.save()
        print("add notify cargo")
    return render(request, 'viewCargo.html')

def send_notification_car(request):
    print("send")
    if request.POST:
        car = Car.objects.get(id=request.POST['car.id'])
        if request.user == car.user:
            return render(request, 'viewCar.html')
        notify = notifyCar(car=car, first_user=request.user, second_user=car.user)
        notify.save()
    return render(request, 'viewCar.html')