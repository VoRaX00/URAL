from django.shortcuts import render
from .models import Cargo, Car, typeBody, typeLoading, carTypeBody, carTypeLoading

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

        id = request.user.id
        cargo = Cargo(name = request.POST['cargoName'], 
            length = request.POST['length'], width = request.POST['width'], height = request.POST['height'],
            weight = request.POST['cargoWeight'], volume = request.POST['volume'], count_place = request.POST['countPlace'],
            loading_data = request.POST['loadingDate'], unloading_data = request.POST['unloadingDate'], phone = request.POST['phone'],
            loading_place = request.POST['loading_address'], unloading_place = request.POST['unloading_address'], bcash=cash, 
            bcashless=cashless, bcashless_nds=nds, bcashless_without_nds=without_nds, price_cash=request.POST['width'],
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
            print(type_body_instance)
            car_type_body = carTypeBody(car=car, type_body=type_body_instance)
            car_type_body.save()

        typesLoading = request.POST.getlist('loadingType')
        for i in typesLoading:
            type_loading_instance = typeLoading.objects.get(name=i)
            print(type_loading_instance)
            car_type_loading = carTypeLoading(car=car, type_loading=type_loading_instance)
            car_type_loading.save()
        
    return render(request, 'addCar.html')

def viewCargo(request):
    cargs = Cargo.objects.all().select_related('user_id')
    
    # for i in cargo:
    #     print(i.name, i.user_id.name, i.user_id.email, i.length, i.width, i.height, i.weight, i.volume, i.count_place,
    #           i.loading_data, i.unloading_data, i.phone, i.loading_place, i.unloading_place, i.bcash, i.bcashless,
    #             i.bcashless_nds, i.bcashless_without_nds, i.price_cash, i.price_cash_nds, i.price_cash_without_nds, i.request_price,
    #             i.comment)
        
    
    context = {
        'cargs' : cargs
    }
    return render(request, 'viewCargo.html', context=context)

class VCar:
    
    def __init__(self, _id, _name, _capacity, _volume, _length, _width, _height, _where_from, _where,
                  _ready_from, _ready_to, _phone, _comment):
        self.name = _name
        self.capacity = _capacity
        self.volume = _volume
        self.legth = _length
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


def viewCar(request):
    # cars = carTypeBody.objects.all().select_related('car__user', 'type_body')
    all_cars = Car.objects.all().select_related('user')
    cars = []
    for i in all_cars:
        car = VCar(i.id, i.car, i.capacity, i.volume, i.length, i.width, i.height, i.where_from, i.where, i.ready_from, i.ready_to, i.phone, i.comment)
        # arr = [str(i.car), str(i.user.name), str(i.capacity), str(i.volume), str(i.length), 
        #        str(i.width), str(i.height), str(i.where_from),
        #        str(i.where), str(i.ready_from), str(i.ready_to), str(i.phone), str(i.comment)]
        
        typesBody = carTypeBody.objects.all().select_related('car', 'type_body')
        # print(typesBody)
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
        'cars': cars
    }
    
    return render(request, 'viewCar.html', context=context)
