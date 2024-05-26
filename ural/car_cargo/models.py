from django.db import models
from user_app.models import User
#from phonenumber_field.modelfields import PhoneNumberField

class Cargo(models.Model):
    name = models.CharField(max_length=255, null=False, unique=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    length = models.PositiveIntegerField(null=False, unique=False)
    width = models.PositiveIntegerField(null=False, unique=False)
    height = models.PositiveIntegerField(null=False, unique=False)

    weight = models.PositiveIntegerField(null=False, unique=False)
    volume = models.PositiveIntegerField(null=False, unique=False)
    count_place = models.PositiveIntegerField(null=False, unique=False)

    loading_data = models.DateField(null=False, unique=False)
    unloading_data = models.DateField(null=False, unique=False)

    phone = models.BigIntegerField(null=False, blank=False, unique=False) #PhoneNumberField(null=False, blank=False, unique=False)

    loading_place = models.TextField(max_length=255, null=False, unique=False)
    unloading_place = models.TextField(max_length=255, null=False, unique=False)

    bcash = models.BooleanField(null=True, unique=False)
    bcashless =  models.BooleanField(null=True, unique=False)
    bcashless_nds = models.BooleanField(null=True, unique=False)
    bcashless_without_nds = models.BooleanField(null=True, unique=False)

    price_cash = models.PositiveIntegerField(null=True, unique=False)
    price_cash_nds = models.PositiveIntegerField(null=True, unique=False)
    price_cash_without_nds = models.PositiveIntegerField(null=True, unique=False)
    request_price = models.BooleanField(null=True, unique=False)

    comment = models.TextField(null=True, unique=False)

    class Meta:
        db_table = 'cargo'

class Car(models.Model):
    car = models.CharField(max_length=200, null=False, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    capacity = models.PositiveIntegerField(null=False, unique=False)
    volume = models.PositiveIntegerField(null=False, unique=False)

    length = models.PositiveIntegerField(null=False, unique=False)
    width = models.PositiveIntegerField(null=False, unique=False)
    height = models.PositiveIntegerField(null=False, unique=False)

    where_from = models.TextField(max_length=255, null=False, unique=False)
    where = models.TextField(max_length=255, null=False, unique=False)

    ready_from = models.DateField(null=False, unique=False)
    ready_to = models.DateField(null=False, unique=False)
    phone = models.BigIntegerField(null=False, blank=False, unique=False) #PhoneNumberField(null=False, blank=False, unique=False)

    comment = models.TextField(null=True, unique=False)

    class Meta:
        db_table = 'car'

class typeBody(models.Model):
    name = models.CharField(max_length=70, null=False, unique=True)

    class Meta:
        db_table = 'type_body'

class carTypeBody(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    type_body = models.ForeignKey(typeBody, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'car_type_body'

class typeLoading(models.Model):
    name = models.CharField(max_length=70, null=False, unique=True)

    class Meta:
        db_table = 'type_loading'

class carTypeLoading(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    type_loading=models.ForeignKey(typeLoading, on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_type_loading'
