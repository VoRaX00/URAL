from django.shortcuts import render

def addCargo(request):
    if request.POST:
        name = request.POST['cargoName']

        length = request.POST['length']
        width = request.POST['width']
        height = request.POST['height']

        weight = request.POST['cargoWeight']
        volume = request.POST['volume']
        count_place = request.POST['countPlace']
        
        loading_date = request.POST['loadingDate']
        print(loading_date)
        unloading_date = request.POST['unloadingDate']

        phone = request.POST['phone']

        loading_place = request.POST['loading_address']
        unloading_place = request.POST['unloading_address']


        if request.POST['cash']:
            cash = request.POST['cash']
        print(cash)

        if request.POST['cashless_payment']:
            cashless_payment = request.POST['cashless_payment']
            if request.POST['without_nds']:
                without_nds = request.POST['without_nds']
                print(without_nds)
                if request.POST['nds']:
                    nds = request.POST['nds']

        price_cash = request.POST['deliveryCostCash']
        price_cash_nds = request.POST['deliveryCostNDS']
        price_cash_without_nds = request.POST['deliveryCostWithoutNDS']

        if request.POST['requestPrice']:
            request_price = request.POST['requestPrice']

        comment = request.POST['comment']

    return render(request, 'addCargo.html')

def addCar(request):
    if request.POST:
        car = request.POST['car']

        type_body = request.POST['bodyType']
        print(type_body)
        type_loading = request.POST['loadingType']

        capacity = request.POST['capacity']
        length = request.POST['length']
        width = request.POST['width']
        height = request.POST['height']
        volume = request.POST['volume']
        
        ready_from = request.POST['readyFrom']
        ready_to = request.POST['readyTo']

        phone = request.POST['phone']

        comment = request.POST['comment']

    return render(request, 'addCar.html')
