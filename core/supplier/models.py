from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL


# table for the supplier 
class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_names = models.CharField(verbose_name='Nombres', max_length=100)
    last_names = models.CharField(verbose_name='Apellidos', max_length=110)
    email = models.EmailField(verbose_name='Correo electrónico', max_length=254)
    image = models.ImageField(upload_to='supplier/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    telephone = models.CharField(verbose_name='Teléfono', max_length=50)
    is_active = models.BooleanField(default=True, verbose_name='¿Activo?')

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
    
    def to_json_faster(self):
        item = {}
        item['id'] = self.id
        item['name'] = self.get_image()
        return item
    
    def __str__(self):
        return self.first_names + ' ' + self.last_names
