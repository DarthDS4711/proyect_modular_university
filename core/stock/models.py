from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from core.product.models import Product

# table stock
class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    # relación de la cantidad de productos que existen dentro de la aplicación 
    product = models.ForeignKey(Product, verbose_name='product_id', on_delete=models.PROTECT, unique=True)
    amount = models.IntegerField(default=0, verbose_name='amount')
    is_activte = models.BooleanField(default=True, verbose_name='is_active')

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['id']
        # nombre de la tabla en la base de datos
        db_table = 'stock'

