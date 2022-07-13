from django import forms
from core.status_send.models import StatusSendSale

class EditStatusSendClientForm(forms.ModelForm):

    class Meta:
        model = StatusSendSale
        exclude = ('sale', 'date_deliver_start', 'date_actual_state')
        widgets = {
            'sale': forms.Select(attrs={
                'class': 'form-control select2'
            }),
            'date_arrival' : forms.DateInput(format='%d-%m-%Y',attrs={
                'type' : 'date',
                'required' : 'false'
            })
        }
