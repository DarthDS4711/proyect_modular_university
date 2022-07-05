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

# modelo que representará el estado de protección de la base de datos 
class SelfProtection(models.Model):
    status_protection_database = models.CharField(verbose_name='Estado proteccion', max_length=512, default='')

    class Meta:
        verbose_name = 'SelfProtection'
        verbose_name_plural = 'SelfProtection'
        ordering = ['id']
        db_table = 'selfprotection'
    
    # sobrescritura del método save, para 
    def save(self, force_insert, force_update, using, update_fields):
        self.status_protection_database = hashlib.sha256(self.status_protection_database).hexdigest()
        return super().save(force_insert, force_update, using, update_fields)
