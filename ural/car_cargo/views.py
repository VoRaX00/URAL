from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from .models import Cargo, Car, TypeBody, TypeLoading, CarTypeBody, CarTypeLoading
from django.core.paginator import Paginator
from notification.models import NotifyCar, NotifyCargo
from django.utils import timezone

def add_cargo(request):
    if request.POST:
        arr_cash = request.POST.getlist('cash')
        cash = False
        cashless = False
        nds = False
        without_nds = False
        if 'cash' in arr_cash:
            cash = True
        if 'cashless' in arr_cash:
            cashless = True
            arr_cash = request.POST.getlist('cashless')
            if 'nds' in arr_cash:
                nds = True
            if 'without_nds' in arr_cash:
                without_nds = True

        arr_cash = request.POST.getlist('request_price')
        request_price = False
        if len(arr_cash) != 0:
            request_price = True

        price_cash = 0
        price_cash_nds = 0
        price_cash_without_nds = 0
        if request.POST.get('deliveryCostCash'):
            price_cash = request.POST.get('deliveryCostCash')
        else:
            price_cash = 0

        if request.POST.get('deliveryCostNDS'):
            price_cash_nds = request.POST.get('deliveryCostNDS')
        else:
            price_cash_nds = 0

        if request.POST.get('deliveryCostWithoutNDS'):
            price_cash_without_nds = request.POST.get('deliveryCostWithoutNDS')
        else:
            price_cash_without_nds = 0

        cargo = Cargo(name=request.POST['cargoName'], length=request.POST['length'], width=request.POST['width'],
                      height=request.POST['height'],
                      weight=request.POST['cargoWeight'], volume=request.POST['volume'],
                      count_place=request.POST['countPlace'],
                      loading_data=request.POST['loadingDate'], unloading_data=request.POST['unloadingDate'],
                      phone=request.POST['phone'],
                      loading_place=request.POST['loading_address'], unloading_place=request.POST['unloading_address'],
                      bcash=cash,
                      bcashless=cashless, bcashless_nds=nds, bcashless_without_nds=without_nds,
                      price_cash=price_cash,
                      price_cash_nds=price_cash_nds,
                      price_cash_without_nds=price_cash_without_nds,
                      request_price=request_price, comment=request.POST['comment'], user_id=request.user)
        cargo.save()
    return render(request, 'addCargo.html')


def add_car(request):
    if request.POST:
        id = request.user.id
        car = Car(car=request.POST['car'], capacity=request.POST['capacity'], volume=request.POST['volume'],
                  length=request.POST['length'], width=request.POST['width'], height=request.POST['height'],
                  where_from=request.POST['place_from'], where=request.POST['place_to'],
                  ready_to=request.POST['readyTo'],
                  ready_from=request.POST['readyFrom'], phone=request.POST['phone'], comment=request.POST['comment'],
                  user_id=id)
        car.save()

        types_body = request.POST.getlist('bodyType')
        for i in types_body:
            type_body_instance = TypeBody.objects.get(name=i)
            car_type_body = CarTypeBody(car=car, type_body=type_body_instance)
            car_type_body.save()

        types_loading = request.POST.getlist('loadingType')
        for i in types_loading:
            type_loading_instance = TypeLoading.objects.get(name=i)
            car_type_loading = CarTypeLoading(car=car, type_loading=type_loading_instance)
            car_type_loading.save()

    return render(request, 'addCar.html')


def view_cargo(request):
    search_name = ''
    if request.POST:
        search_name = request.POST.get('search_input')

    user_id = request.user.id
    if search_name != '':
        today = timezone.now().date()
        cargs = Cargo.objects.all().filter(name=search_name).filter(loading_data__gt=today).select_related('user_id').exclude(user_id=user_id).order_by(
            '-id')
    else:
        today = timezone.now().date()
        cargs = Cargo.objects.all().filter(loading_data__gt=today).select_related('user_id').exclude(user_id=user_id).order_by('-id')

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


def array_cars(all_cars):
    cars = []
    for i in all_cars:
        car = VCar(i.id, i.car, i.capacity, i.volume, i.length, i.width, i.height, i.where_from, i.where, i.ready_from,
                   i.ready_to, i.phone, i.comment, )
        types_body = CarTypeBody.objects.all().select_related('car', 'type_body')
        check = False
        j = 0
        k = 0
        while j < len(types_body):
            if types_body[j].car.id == i.id:
                car.type_body.append(types_body[j].type_body.name)
                check = True
            elif check:
                break
            j += 1

        check = False
        types_loading = CarTypeLoading.objects.all().select_related('car', 'type_loading')
        while k < len(types_loading):
            if types_loading[k].car.id == i.id:
                car.type_loading.append(types_loading[k].type_loading.name)
                check = True
            elif check:
                break

            k += 1
        cars.append(car)
    return cars


def view_car(request):
    search_name = ''
    if request.POST:
        search_name = request.POST.get('search_input')

    if search_name != '':
        today = timezone.now().date()
        all_cars = Car.objects.all().filter(car=search_name).filter(ready_from__gt=today).select_related('user').exclude(user=request.user.id).order_by('-id')
        cars = array_cars(all_cars)
    else:
        today = timezone.now().date()
        all_cars = Car.objects.all().filter(ready_from__gt=today).select_related('user').exclude(user=request.user.id).order_by('-id')
        cars = array_cars(all_cars)

    paginator = Paginator(cars, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'viewCar.html', context=context)


#не введено пока что в основной проект
def edit_car(post):
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
        type_body_instance = TypeBody.objects.get(name=i)
        car_type_body = CarTypeBody(car=car, type_body=type_body_instance)
        #car_type_body.save()

    typesLoading = post.getlist('loadingType')
    for i in typesLoading:
        type_loading_instance = TypeLoading.objects.get(name=i)
        car_type_loading = CarTypeLoading(car=car, type_loading=type_loading_instance)
        #car_type_loading.save()


def edit_cargo(post):
    cargo_id = post['cargo_id']

    try:
        cargo = Cargo.objects.get(id=cargo_id)

        arr_cash = post.getlist('cash')
        if 'cash' in arr_cash:
            cargo.bcash = True

        if 'cashless' in arr_cash:
            cargo.bcashless = True
            arr_cash = post.getlist('cashless')
            if 'nds' in arr_cash:
                cargo.bcashless_nds = True
            if 'without_nds' in arr_cash:
                cargo.bcashless_without_nds = True

        arr_cash = post.getlist('request_price')

        if len(arr_cash) != 0:
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


def my_car(request):
    if request.POST:
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        if not csrf_token == request.COOKIES.get('csrfmiddlewaretoken'):
            return HttpResponseForbidden("CSRF Token не действителен.")
        edit_car(request.POST)

    all_cars = Car.objects.all().select_related('user').filter(user_id=request.user).order_by('-id')
    cars = array_cars(all_cars)

    paginator = Paginator(cars, per_page=4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'MyCar.html', context=context)


def my_cargo(request):
    if request.POST:
        edit_cargo(request.POST)

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
        notify = NotifyCargo(cargo=cargo, first_user=request.user, second_user=cargo.user_id)
        notify.save()
    return view_cargo(request)


def send_notification_car(request):
    if request.POST:
        car = Car.objects.get(id=request.POST.get('car_id'))
        if request.user == car.user:
            return render(request, 'viewCar.html')
        notify = NotifyCar(car=car, first_user=request.user, second_user=car.user)
        notify.save()
    return view_car(request)
