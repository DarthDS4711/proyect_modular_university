# Generated by Django 4.0.3 on 2022-04-26 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20220219_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='warranty_id',
        ),
    ]