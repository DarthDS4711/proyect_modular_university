# Generated by Django 4.0.3 on 2022-05-17 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_send', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statussendsale',
            name='date_actual_state',
            field=models.DateField(default=datetime.datetime.now, verbose_name='date_actual_state'),
        ),
        migrations.AddField(
            model_name='statussendsale',
            name='date_deliver_start',
            field=models.DateField(default=datetime.datetime.now, verbose_name='date_deliver_start'),
        ),
    ]