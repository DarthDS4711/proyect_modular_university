from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from core.sale.models import Sale


# table for the status in the sale
class StatusSend(models.Model):
    description = models.CharField(verbose_name='Descripción', max_length=180)


    class Meta:
        verbose_name = "StatusSend"
        verbose_name_plural = 'StatusSends'
        ordering = ['id']
        db_table = 'status_send'

    def __str__(self) -> str:
        return f'{self.description}' 


# table for the status of the send of the a sale
class StatusSendSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    sale = models.ForeignKey(Sale, verbose_name='Número de factura', on_delete=models.PROTECT, unique=True)
    date_arrival = models.DateField(default=datetime.now, verbose_name='Fecha llegada')
    status_send = models.ForeignKey(StatusSend, verbose_name='Estado de envio', on_delete=models.PROTECT)
    delivered = models.BooleanField(default=False, verbose_name='¿Entregada?')
    date_deliver_start = models.DateField(default=datetime.now, verbose_name='Fecha inicio envio')
    date_actual_state = models.DateField(default=datetime.now, verbose_name='Fecha actualización envio')


    class Meta:
        verbose_name = "StatusSendSale"
        verbose_name_plural = 'StatusSendSales'
        ordering = ['id']
        db_table = 'status_send_sale' 
