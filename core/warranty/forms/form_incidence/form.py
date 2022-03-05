from django import forms
from core.warranty.models import Incidence


class IncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Nombre de la incidencia'
            }),
            'description' : forms.TextInput(attrs={
                'placeholder' : 'Descripción de la incidencia'
            })
        }