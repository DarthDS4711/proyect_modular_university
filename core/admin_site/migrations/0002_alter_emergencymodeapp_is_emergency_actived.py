# Generated by Django 4.0.3 on 2022-10-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencymodeapp',
            name='is_emergency_actived',
            field=models.BooleanField(default=False, verbose_name='¿Activado?'),
        ),
    ]
