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
            request_price=request_price, comment = request.POST['comment'], user_id = id)
        
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
    return render(request, 'viewCargo.html')

def viewCar(request):
    return render(request, 'viewCar.html')
