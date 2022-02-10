from datetime import datetime
from django.db import models
from django.forms import model_to_dict


# table incidence
class Incidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)

    class Meta:
         verbose_name = "Incidence"
         verbose_name_plural = 'Incidences'
         ordering = ['id']
         db_table = 'incidence'

# table warranty for user of the application
class WarrantySale(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)
    months_coverred = models.IntegerField(default=3, verbose_name='months_covered')
    incidence = models.ManyToManyField(Incidence, verbose_name='incidence_id')

    class Meta:
        verbose_name = "WarrantySale"
        verbose_name_plural = 'WarrantySales'
        ordering = ['id']
        db_table = 'warranty_sale'

# table warranty for admin of the application
class WarrantyPurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)
    months_coverred = models.IntegerField(default=3, verbose_name='months_covered')
    incidence = models.ManyToManyField(Incidence, verbose_name='incidence_id')

    class Meta:
        verbose_name = "WarrantyPurchase"
        verbose_name_plural = 'WarrantyPurchases'
        ordering = ['id']
        db_table = 'warranty_purchase'


