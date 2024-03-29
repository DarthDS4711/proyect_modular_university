from re import T
from django.db import models
from core.product.models import Product


# table incidence
class Incidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='name_incidence', max_length=40, null=True)
    description = models.CharField(verbose_name='description', max_length=150)
    is_active = models.BooleanField(default=True)

    class Meta:
         verbose_name = "Incidence"
         verbose_name_plural = 'Incidences'
         ordering = ['id']
         db_table = 'incidence'
    

    def __str__(self):
        return f'{self.name}'

# table warranty for user of the application
class WarrantySale(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre', default='', max_length=80)
    description = models.CharField(verbose_name='Descripción', max_length=150)
    months_coverred = models.IntegerField(default=3, verbose_name='Meses cubiertos')
    incidence = models.ManyToManyField(Incidence, verbose_name='Incidencia')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "WarrantySale"
        verbose_name_plural = 'WarrantySales'
        ordering = ['id']
        db_table = 'warranty_sale'
    
    def __str__(self):
        return f'{self.name}'


# table for create a relation between product and warranty
class WarrantyProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    # el producto no puede tener más de una garantía, pero la garantía si puede aparecer más veces
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, unique=True, verbose_name='Producto')
    warranty = models.ForeignKey(WarrantySale, on_delete=models.PROTECT, null=True, verbose_name='Garantía')

    class Meta:
        verbose_name = "WarrantyProduct"
        verbose_name_plural = 'WarrantyProduct'
        ordering = ['id']
        db_table = 'warranty_product'
    



