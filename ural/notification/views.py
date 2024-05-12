from django.shortcuts import render
from .models import notifyCargo, notifyCar
from car_cargo.models import Cargo, carTypeBody, carTypeLoading
from car_cargo.views import VCar

def my_notification(request):
    notifications_cargo = notifyCargo.objects.all().filter(second_user=request.user).order_by("-id")
    notifications_car = notifyCar.objects.all().filter(second_user=request.user).order_by("-id")
    
    cargs = []
    cars = []
    for i in notifications_cargo:
        cargo = Cargo.objects.get(id = i.cargo.id)
        cargs.append(cargo)
    
    for i in notifications_car:
        car = VCar(i.car.id, i.car.car, i.car.capacity, i.car.volume, i.car.length, i.car.width, 
                   i.car.height, i.car.where_from, i.car.where, i.car.ready_from, i.car.ready_to, 
                   i.car.phone, i.car.comment,)
        
        typesBody = carTypeBody.objects.all().select_related('car', 'type_body')
        check = False
        j=0
        k=0
        while j < len(typesBody):
            if typesBody[j].car.id == i.id:
                car.type_body.append(typesBody[j].type_body.name)
                check = True
            elif check:
                break
                
            j+=1

        check = False
        typesLoading = carTypeLoading.objects.all().select_related('car', 'type_loading')
        while k < len(typesLoading):
            if typesLoading[k].car.id == i.id:
                car.type_loading.append(typesLoading[k].type_loading.name)
                check=True
            elif check:
                break
                
            k+=1

        cars.append(car)

    context = {
        'cargo' : cargs,
        'car' : cars,
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