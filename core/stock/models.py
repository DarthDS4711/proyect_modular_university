from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from core.product.models import Product, Size
from django.contrib.postgres.fields import ArrayField

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
    
    def __str__(self):
        return f'Stock producto: {self.product.name}'
    
    def calculate_amount(self):
        ammount = 0
        stock_sizes = StockProductSize.objects.filter(stock = self)
        for stock in stock_sizes:
            ammount += stock.amount
        self.amount = ammount

# stock por el tamaño de la prenda
class StockProductSize(models.Model):
    id = models.BigAutoField(primary_key=True)
    stock = models.ForeignKey(Stock, verbose_name='stock', on_delete=models.PROTECT, null=True)
    size = models.ForeignKey(Size, verbose_name='size', on_delete=models.PROTECT)
    amount = models.IntegerField(default=0, verbose_name='amount')

    class Meta:
        verbose_name = 'StockProductSize'
        verbose_name_plural = 'StockProductSizes'
        ordering = ['id']
        # nombre de la tabla en la base de datos
        db_table = 'stock_product_sizes'
    
    def __str__(self):
        return f'Stock talla: {self.size.size_product}'


