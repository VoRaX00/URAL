# Generated by Django 5.0.4 on 2024-04-24 13:55

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=200)),
                ('type_body', models.CharField(max_length=200)),
                ('type_loading', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField()),
                ('volume', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('where_from', models.TextField(max_length=255)),
                ('where', models.TextField(max_length=255)),
                ('ready_from', models.DateField()),
                ('ready_to', models.DateField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('comment', models.TextField(null=True)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('id_user', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('volume', models.PositiveIntegerField()),
                ('count_place', models.PositiveIntegerField()),
                ('loading_data', models.DateField()),
                ('unloading_data', models.DateField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('loading_place', models.TextField(max_length=255)),
                ('unloading_place', models.TextField(max_length=255)),
                ('bcash', models.BooleanField(null=True)),
                ('bcashless', models.BooleanField(null=True)),
                ('bcashless_nds', models.BooleanField(null=True)),
                ('bcashless_without_nds', models.BooleanField(null=True)),
                ('price_cash', models.PositiveIntegerField(null=True)),
                ('price_cash_nds', models.PositiveIntegerField(null=True)),
                ('price_cash_without_nds', models.PositiveIntegerField(null=True)),
                ('request_price', models.BooleanField(null=True)),
                ('comment', models.TextField(null=True)),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
    ]