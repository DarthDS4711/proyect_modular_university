from django import forms
from core.sale.models import Sale
from core.status_send.models import StatusSend, StatusSendSale


class StatusSendClientForm(forms.ModelForm):

    date_arrival = forms.DateField(
            widget=forms.DateInput(format=('%d-%m-%Y'),
            attrs={
                'class': 'datepicker', 
                'placeholder': 
                'Select a date', 
                'type': 'date'
            }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sale'].queryset = Sale.objects.none()
    
    class Meta:
        model = StatusSendSale
        exclude = ('delivered', 'date_deliver_start', 'date_actual_state')
        widgets = {
            'sale' : forms.Select(attrs={
                'class' : 'form-control select2'
            })
        }
    