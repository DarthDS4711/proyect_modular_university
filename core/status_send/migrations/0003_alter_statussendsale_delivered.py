# Generated by Django 4.0.3 on 2022-05-18 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_send', '0002_statussendsale_date_actual_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statussendsale',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
