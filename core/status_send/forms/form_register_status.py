from dataclasses import fields
from django import forms
from core.status_send.models import StatusSend


class StatusSendForm(forms.ModelForm):
    
    class Meta:
        model = StatusSend
        fields = '__all__'
        widgets = {
            'description' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese el nombre del estado'
            })
        }