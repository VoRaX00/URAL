from django.shortcuts import render
from .models import notifyCargo, notifyCar
from car_cargo.models import Cargo, carTypeBody, carTypeLoading
from car_cargo.views import VCar
from django.core.paginator import Paginator

class ObjectNotify:
    def __init__(self, id, cargo=None, car=None, isCar=False):
        self.cargo = cargo
        self.car = car
        self.id = id
        self.isCar = isCar
    

def objectsNotify(cargs, cars):
    objects=[]
    i=0
    j=0
    while i < len(cargs) and j < len(cars):
        if cargs[i].id < cars[j].id:
            objects.append(ObjectNotify(id=cars[j].id, car=cars[j]))
            j+=1
        else:
            objects.append(ObjectNotify(id=cargs[i].id, cargo=cargs[i]))
            i+=1

    if i < len(cargs):
        while i < len(cargs):
            objects.append(ObjectNotify(id=cargs[i].id, cargo=cargs[i]))
            i+=1
    else:
        while j < len(cars):
            objects.append(ObjectNotify(id=cars[j], car=cars[j], isCar=True))
            j+=1
    return objects

def arrayCars(cars):
    array=[]
    for i in cars:
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
        array.append(car)
    return array

def arrayCargs(cargs):
    array = []
    for i in cargs:
        cargo = Cargo.objects.get(id = i.cargo.id)
        array.append(cargo)
    return array
        
def my_notification(request):
    notifications_cargo = notifyCargo.objects.all().filter(second_user=request.user).order_by("-id")
    notifications_car = notifyCar.objects.all().filter(second_user=request.user).order_by("-id")

    cargs = arrayCargs(notifications_cargo)
    cars = arrayCars(notifications_car)
    objects = objectsNotify(cargs, cars)

    paginator = Paginator(objects, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj
    }
    return render(request, 'MyNotification.html', context=context)

def my_responses(request):
    notifications_cargo = notifyCargo.objects.all().filter(first_user=request.user).order_by("-id")
    notifications_car = notifyCar.objects.all().filter(first_user=request.user).order_by("-id")
    
    cargs = arrayCargs(notifications_cargo)
    cars = arrayCars(notifications_car)
    objects = objectsNotify(cargs, cars)

    paginator = Paginator(objects, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj
    }

    return render(request, 'MyResponses.html', context=context)