from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import MEDIA_URL, STATIC_URL
from core.user.choises import gender_choices
from django.core.validators import MaxValueValidator, MinValueValidator


# modificación del modelo de usuario a usar en django
# en el cual solo se agregarán o en su defecto
# modificarán los campos existentes en django
class User(AbstractUser):
    # modificación el id del usuario
    id = models.BigAutoField(primary_key=True)
    # campo de imagen para el usuario
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    date_birthday = models.DateField(default=datetime.now, verbose_name='date_birthday')
    gender = models.CharField(verbose_name='gender', max_length=10, choices=gender_choices, default='male')
    # sobreescritura del campo email para establecerlo como campo único
    email = models.EmailField(verbose_name='email', blank=True, unique=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
        db_table = 'user'


#Modelo relacionado a la agenda de direcciones del usuario
class DirectionUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, verbose_name='nombre direccion')
    street = models.CharField(max_length=80, verbose_name='calle', blank=True)
    postal_code = models.IntegerField(verbose_name='codigo postal', validators=[
        # formato de validación para el código postal méxicano
        MaxValueValidator(99999),
        MinValueValidator(10000)
    ], default=10000)
    exterior_number = models.CharField(max_length=15, verbose_name='Numero exterior', default='')
    interior_number = models.CharField(max_length=15, verbose_name='Numero interior', default='')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name='Activo?', default=True)


    def __str__(self):
        return f'{self.name}'
    

    class Meta:
        verbose_name = 'DirectionUser'
        verbose_name_plural = 'DirectionUsers'
        ordering = ['id']
        db_table = 'directionuser'
