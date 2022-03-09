from datetime import datetime
from django.db import models
from django.forms import model_to_dict


# table for the supplier 
class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_names = models.CharField(verbose_name='first_names', max_length=100)
    last_names = models.CharField(verbose_name='last_names', max_length=110)
    email = models.EmailField(verbose_name='email', max_length=254)
    image = models.ImageField(upload_to='supplier/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    telephone = models.CharField(verbose_name='telephone', max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = 'Supplier'
        ordering = ['id']
        db_table = 'supplier'
