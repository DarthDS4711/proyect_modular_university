from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from core.user.models import User
from core.product.models import Product, Size


# table for the sale in the app
class Sale(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='user_id', on_delete=models.PROTECT)
    date_sale = models.DateField(default=datetime.now, verbose_name='date_sale')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='subtotal')
    iva = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='iva', default=0.16)
    total = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='iva')


    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = 'Sales'
        ordering = ['id']
        db_table = 'sale'

# table for the detail of the sale
class DetailSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    sale = models.ForeignKey(Sale, verbose_name='sale_id', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='product_id', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='price')
    ammount = models.IntegerField(default=0, verbose_name='ammount')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='subtotal')
    color = models.CharField(max_length=8, default='')
    size = models.ForeignKey(Size, verbose_name='size_id', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "DetailSale"
        verbose_name_plural = 'DetailSales'
        ordering = ['id']
        db_table = 'detail_sale'
