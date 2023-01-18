# Generated by Django 4.0.3 on 2022-10-19 04:37

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_directionuser_exterior_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directionuser',
            name='exterior_number',
            field=models.CharField(default='', max_length=15, verbose_name='Número exterior'),
        ),
        migrations.AlterField(
            model_name='directionuser',
            name='interior_number',
            field=models.CharField(default='', max_length=15, verbose_name='Núsmero interior'),
        ),
        migrations.AlterField(
            model_name='directionuser',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='directionuser',
            name='postal_code',
            field=models.IntegerField(default=10000, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)], verbose_name='Código postal'),
        ),
        migrations.AlterField(
            model_name='directionuser',
            name='street',
            field=models.CharField(blank=True, max_length=80, verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_birthday',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d', verbose_name='Imagen'),
        ),
    ]
