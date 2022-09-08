from datetime import datetime
from django.db import models
from core.product.models import Product, Size


# table for the purchase
class Purchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_purchase = models.DateField(default=datetime.now, verbose_name='Fecha factura')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Iva', default=0.16)
    total = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Total')

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = 'Purchases'
        ordering = ['id']
        db_table = 'purchase'

# table for the detail of the sale
class DetailPurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, verbose_name='Número factura', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio')
    ammount = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Subtotal')
    size = models.ForeignKey(Size, verbose_name='Talla', on_delete=models.PROTECT, null=True)
    color = models.CharField(max_length=8, default='')

    class Meta:
        verbose_name = "DetailPurchase"
        verbose_name_plural = 'DetailPurchase'
        ordering = ['id']
        db_table = 'detail_purchase'
