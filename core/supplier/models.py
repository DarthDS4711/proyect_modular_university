from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL


# table for the supplier 
class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_names = models.CharField(verbose_name='first_names', max_length=100)
    last_names = models.CharField(verbose_name='last_names', max_length=110)
    email = models.EmailField(verbose_name='email', max_length=254)
    image = models.ImageField(upload_to='supplier/%Y/%m/%d', null=True, blank=True, verbose_name='image')
    telephone = models.CharField(verbose_name='telephone', max_length=50)
    is_active = models.BooleanField(default=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def get_name(self):
        return self.first_names + ' ' + self.last_names

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = 'Supplier'
        ordering = ['id']
        db_table = 'supplier'
