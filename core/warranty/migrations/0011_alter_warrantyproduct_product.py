# Generated by Django 4.0.3 on 2022-04-27 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_product_colors_product_last_color_and_more'),
        ('warranty', '0010_delete_warrantypurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrantyproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.product', unique=True),
        ),
    ]
