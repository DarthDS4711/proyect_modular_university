# Generated by Django 4.0.3 on 2022-04-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_directionuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='directionuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]