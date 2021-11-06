from datetime import datetime
from django.db import models
from django.forms import model_to_dict

# table warranty for user of the application
class WarrantySale(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)
    date_start = models.DateField(default=datetime.now, verbose_name='date_start')
    date_end = models.DateField(default=datetime.now, verbose_name='date_end')

    class Meta:
        verbose_name = "WarrantySale"
        verbose_name_plural = 'WarrantySales'
        ordering = ['id']
        db_table = 'warranty_sale'

# table warranty for admin of the application
class WarrantyPurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)
    date_start = models.DateField(default=datetime.now, verbose_name='date_start')
    date_end = models.DateField(default=datetime.now, verbose_name='date_end')

    class Meta:
        verbose_name = "WarrantyPurchase"
        verbose_name_plural = 'WarrantyPurchases'
        ordering = ['id']
        db_table = 'warranty_purchase'


# table type_incidence
class TypeIncidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    # nombre del tipo de la incidencia 
    name_type_incidence = models.CharField(verbose_name='name_incidence', max_length=150)

    class Meta:
         verbose_name = "TypeIncidence"
         verbose_name_plural = 'TypeIncidences'
         ordering = ['id']
         db_table = 'type_incidence'

# table incidence
class Incidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(verbose_name='description', max_length=150)
    # tipo de incidencia dada por la llave foranea
    type_incidence = models.ForeignKey(TypeIncidence, verbose_name='type_incidence', on_delete=models.PROTECT)
    covered_months = models.IntegerField(default=0, verbose_name='covered_months')

    class Meta:
         verbose_name = "Incidence"
         verbose_name_plural = 'Incidences'
         ordering = ['id']
         db_table = 'incidence'


# table for relation the incedence with the warranty of the sale
class WarrantyIncidenceSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    warranty_sale = models.ForeignKey(WarrantySale, verbose_name='warranty_sale_id', on_delete=models.PROTECT)
    incidence = models.ForeignKey(Incidence, verbose_name='incidence_id', on_delete=models.PROTECT)

    class Meta:
         verbose_name = "WarrantyIncidenceSale"
         verbose_name_plural = 'WarrantyIncidenceSales'
         ordering = ['id']
         db_table = 'warranty_incidence_sale'

# table for relation the incedence with the warranty of the purchase
class WarrantyIncidencePurchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    warranty_purchase = models.ForeignKey(WarrantyPurchase, verbose_name='warranty_sale_id', on_delete=models.PROTECT)
    incidence = models.ForeignKey(Incidence, verbose_name='incidence_id', on_delete=models.PROTECT)

    class Meta:
         verbose_name = "WarrantyIncidencePurchase"
         verbose_name_plural = 'WarrantyIncidencePurchases'
         ordering = ['id']
         db_table = 'warranty_incidence_purchase'


