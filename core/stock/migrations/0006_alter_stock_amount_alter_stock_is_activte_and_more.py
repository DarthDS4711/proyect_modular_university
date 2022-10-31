# Generated by Django 4.0.3 on 2022-10-19 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_category_description_alter_category_image_and_more'),
        ('stock', '0005_remove_stock_ammount_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='is_activte',
            field=models.BooleanField(default=True, verbose_name='¿Activo?'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', unique=True, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='stockproductsize',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='stockproductsize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.size', verbose_name='Talla'),
        ),
        migrations.AlterField(
            model_name='stockproductsize',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.stock', verbose_name='Número stock'),
        ),
    ]
