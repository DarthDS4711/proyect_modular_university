# Generated by Django 4.0.3 on 2022-04-28 15:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stockproductsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ammount_size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(default=0), null=True, size=10),
        ),
    ]