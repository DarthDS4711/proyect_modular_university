# Generated by Django 4.0.3 on 2022-05-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_remove_purchase_warranty_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='supplier',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.16, max_digits=3, verbose_name='iva'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=18, verbose_name='total'),
        ),
    ]
