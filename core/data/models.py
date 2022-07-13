from django.db import models
import hashlib

# modelo que representará la autoreplicación de la base de datos
# al momento de realizar cualquier cambio en la aplicacion
class DataReplication(models.Model):
    autoreplication = models.BooleanField(verbose_name='autoreplicacion', default=True)

    class Meta:
        verbose_name = "DataReplication"
        verbose_name_plural = 'DataReplicacions'
        ordering = ['id']
        db_table = 'datareplication'


