# Generated by Django 4.0.3 on 2022-04-27 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_colors_product_last_color_and_more'),
        ('stock', '0002_alter_stock_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockProductSize',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0, verbose_name='amount')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.size', verbose_name='size')),
            ],
            options={
                'verbose_name': 'StockProductSize',
                'verbose_name_plural': 'StockProductSizes',
                'db_table': 'stock_product_sizes',
                'ordering': ['id'],
            },
        ),
    ]
