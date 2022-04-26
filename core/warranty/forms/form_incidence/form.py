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
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data