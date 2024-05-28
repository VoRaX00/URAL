from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from .models import Cargo, Car, typeBody, typeLoading, carTypeBody, carTypeLoading
from django.core.paginator import Paginator
from notification.models import notifyCar, notifyCargo

def addCargo(request):
    if request.POST:
        arrCash = request.POST.getlist('cash')
        cash=False
        cashless = False
        nds = False
        without_nds = False
        if 'cash' in arrCash:
            cash=True
        if 'cashless' in arrCash:
            cashless = True
            arrCash = request.POST.getlist('cashless')
            if 'nds' in arrCash:
                nds=True
            if 'without_nds' in arrCash:
                without_nds=True
        
        arrCash = request.POST.getlist('request_price')
        request_price = False
        if len(arrCash) != 0:
            request_price = True

        cargo = Cargo(name = request.POST['cargoName'], 
            length = request.POST['length'], width = request.POST['width'], height = request.POST['height'],
            weight = request.POST['cargoWeight'], volume = request.POST['volume'], count_place = request.POST['countPlace'],
            loading_data = request.POST['loadingDate'], unloading_data = request.POST['unloadingDate'], phone = request.POST['phone'],
            loading_place = request.POST['loading_address'], unloading_place = request.POST['unloading_address'], bcash=cash, 
            bcashless=cashless, bcashless_nds=nds, bcashless_without_nds=without_nds, price_cash=request.POST['deliveryCostCash'],
            price_cash_nds = request.POST['deliveryCostNDS'], price_cash_without_nds = request.POST['deliveryCostWithoutNDS'], 
            request_price=request_price, comment = request.POST['comment'], user_id = request.user)
         
        cargo.save()
    return render(request, 'addCargo.html')

def addCar(request):
    if request.POST:
        id = request.user.id
        car = Car(car=request.POST['car'],capacity = request.POST['capacity'], volume = request.POST['volume'], 
                length = request.POST['length'], width = request.POST['width'], height = request.POST['height'], 
                where_from=request.POST['place_from'], where=request.POST['place_to'], ready_to = request.POST['readyTo'],
                ready_from = request.POST['readyFrom'], phone = request.POST['phone'], comment = request.POST['comment'], user_id=id)
        car.save()

        typesBody = request.POST.getlist('bodyType')
        for i in typesBody:
            type_body_instance = typeBody.objects.get(name=i)
            car_type_body = carTypeBody(car=car, type_body=type_body_instance)
            car_type_body.save()

        typesLoading = request.POST.getlist('loadingType')
        for i in typesLoading:
            type_loading_instance = typeLoading.objects.get(name=i)
            car_type_loading = carTypeLoading(car=car, type_loading=type_loading_instance)
            car_type_loading.save()
        
    return render(request, 'addCar.html')

def viewCargo(request):
    user_id = request.user.id
    cargs = Cargo.objects.all().select_related('user_id').exclude(user_id=user_id).order_by('-id')
    paginator = Paginator(cargs, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'viewCargo.html', context=context)

class VCar:
    
    def __init__(self, _id, _name, _capacity, _volume, _length, _width, _height, _where_from, _where,
                  _ready_from, _ready_to, _phone, _comment):
        self.name = _name
        self.capacity = _capacity
        self.volume = _volume
        self.length = _length
        self.width = _width
        self.height = _height
        self.where_from = _where_from
        self.where = _where
        self.ready_from = _ready_from
        self.ready_to = _ready_to
        self.id = _id
        self.phone = _phone
        self.comment = _comment
        self.type_body = []
        self.type_loading = []

def arrayCars(all_cars):
    cars=[]
    for i in all_cars:
        car = VCar(i.id, i.car, i.capacity, i.volume, i.length, i.width, i.height, i.where_from, i.where, i.ready_from, i.ready_to, i.phone, i.comment,)
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
    return cars

def viewCar(request):
    all_cars = Car.objects.all().select_related('user').exclude(user=request.user.id).order_by('-id')
    cars = arrayCars(all_cars)

    paginator = Paginator(cars, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    
    return render(request, 'viewCar.html', context=context)

#не введено пока что в основной проект
def editCar(post): 
    car_id = post['car_id']
    car = Car.objects.get(id=car_id)
    car.car = post['car']
    car.capacity = post['capacity']
    car.volume = post['volume']
    car.length = post['length']
    car.width = post['width']
    car.height = post['height']
    car.where_from = post['place_from']
    car.where = post['place_to']
    car.ready_to = post['readyTo']
    car.ready_from = post['readyFrom']
    car.phone = post['phone']
    car.comment = post['comment']
    #car.save()

    #дописать удаление всех типов кузова и потом добавление новых типов кузова
    typesBody = post.getlist('bodyType')
    for i in typesBody:
        type_body_instance = typeBody.objects.get(name=i)
        car_type_body = carTypeBody(car=car, type_body=type_body_instance)
        #car_type_body.save()

    typesLoading = post.getlist('loadingType')
    for i in typesLoading:
        type_loading_instance = typeLoading.objects.get(name=i)
        car_type_loading = carTypeLoading(car=car, type_loading=type_loading_instance)
        #car_type_loading.save()

def editCargo(post):
    cargo_id = post['cargo_id']
        
    try:
        cargo = Cargo.objects.get(id=cargo_id)

        arrCash = post.getlist('cash')
        if 'cash' in arrCash:
            cargo.bcash = True

        if 'cashless' in arrCash:
            cargo.bcashless = True
            arrCash = post.getlist('cashless')
            if 'nds' in arrCash:
                cargo.bcashless_nds=True
            if 'without_nds' in arrCash:
                cargo.bcashless_without_nds=True
        
        arrCash = post.getlist('request_price')

        if len(arrCash) != 0:
            cargo.request_price = True

        cargo.name = post['cargoName']
        cargo.length = post['length']
        cargo.width = post['width']
        cargo.height = post['height']
        cargo.weight = post['cargoWeight']
        cargo.volume = post['volume']
        cargo.count_place = post['countPlace']
        cargo.loading_data = post['loadingDate']
        cargo.unloading_data = post['unloadingDate']
        cargo.phone = post['phone']
        cargo.loading_place = post['loading_address']
        cargo.unloading_place = post['unloading_address']
        cargo.price_cash = post['deliveryCostCash']
        cargo.price_cash_nds = post['deliveryCostNDS']
        cargo.price_cash_without_nds = post['deliveryCostWithoutNDS']
        cargo.comment = post['comment']
    
        cargo.save()

    except ObjectDoesNotExist:
        return HttpResponseForbidden("груза с таким id не существует")

def myCar(request):
    if request.POST:
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        if not csrf_token == request.COOKIES.get('csrfmiddlewaretoken'):
            return HttpResponseForbidden("CSRF Token не действителен.")
        editCar(request.POST)
        
    all_cars = Car.objects.all().select_related('user').filter(user_id=request.user).order_by('-id')
    cars = arrayCars(all_cars)

    paginator = Paginator(cars, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'MyCar.html', context=context)

def myCargo(request):
    if request.POST:
        editCargo(request.POST) 

    cargs = Cargo.objects.all().select_related('user_id').filter(user_id=request.user).order_by('-id')
    paginator = Paginator(cargs, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'MyCargo.html', context=context)

def send_notification_cargo(request):
    if request.POST:
        cargo = Cargo.objects.get(id=request.POST.get('cargo_id'))
        if request.user == cargo.user_id:
            return render(request, 'viewCargo.html')
        notify = notifyCargo(cargo=cargo, first_user=request.user, second_user=cargo.user_id)
        notify.save()
    return viewCargo(request)

def send_notification_car(request):
    if request.POST:
        car = Car.objects.get(id=request.POST.get('car_id'))
        if request.user == car.user:
            return render(request, 'viewCar.html')
        notify = notifyCar(car=car, first_user=request.user, second_user=car.user)
        notify.save()
    return viewCar(request)
