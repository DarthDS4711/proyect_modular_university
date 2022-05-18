from django import forms
from core.sale.models import Sale
from core.status_send.models import StatusSend, StatusSendSale


class EditStatusSendClientForm(forms.ModelForm):

    class Meta:
        model = StatusSendSale
        exclude = ('sale', 'date_arrival', 'date_deliver_start', 'date_actual_state')
        widgets = {
            'sale': forms.Select(attrs={
                'class': 'form-control select2'
            })
        }
