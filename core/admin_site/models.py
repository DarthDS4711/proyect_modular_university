from django.db import models

# clase que nos modelará si la pagina ha entrado a un modo de emergencia
class EmergencyModeApp(models.Model):
    is_emergency_actived = models.BooleanField(default=False, verbose_name='¿Activado?')

    class Meta:
         verbose_name = "EmergencyModeApp"
         verbose_name_plural = 'EmergencyModeApp'
         ordering = ['id']
         db_table = 'emergencymodeapp'


