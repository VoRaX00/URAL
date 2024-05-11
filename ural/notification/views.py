from django.shortcuts import render
from .models import notifyCargo, notifyCar
from car_cargo.models import Cargo, Car
# Create your views here.

def my_notification(request):
    notifications_cargo = notifyCargo.objects.all().filter(second_user=request.user).order_by("-id")
    notifications_car = notifyCar.objects.all().filter(second_user=request.user).order_by("-id")
    #добавить отображение карточек на странице. соответ-но доставать данные о машине или грузе из бд)
    context = {
        'cargo' : notifications_cargo,
        'car' : notifications_car,
    }
    return render(request, 'MyNotification.html', context=context)

def my_responses(request):
    notifications_cargo = notifyCargo.objects.all().filter(first_user=request.user).order_by("-id")
    notifications_car = notifyCar.objects.all().filter(first_user=request.user).order_by("-id")
    #добавить отображение карточек на странице. соответ-но доставать данные о машине или грузе из бд)
    
    context = {
        'cargo' : notifications_cargo,
        'car' : notifications_car,
    }
    return render(request, 'MyResponses.html', context=context)