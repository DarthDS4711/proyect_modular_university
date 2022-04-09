from datetime import datetime
from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import UUIDField
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser
from config.settings import MEDIA_URL, STATIC_URL
from core.user.choises import gender_choices


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

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
        db_table = 'user'
    
