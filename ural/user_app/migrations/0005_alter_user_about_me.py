# Generated by Django 5.0.4 on 2024-05-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_user_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.TextField(default='Пусто', max_length=700),
        ),
    ]