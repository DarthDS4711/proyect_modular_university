# Generated by Django 4.0.3 on 2022-10-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='first_names',
            field=models.CharField(max_length=100, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='supplier/%Y/%m/%d', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='¿Activo?'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='last_names',
            field=models.CharField(max_length=110, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='telephone',
            field=models.CharField(max_length=50, verbose_name='Teléfono'),
        ),
    ]