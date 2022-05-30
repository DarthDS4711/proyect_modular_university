from django import forms

from core.warranty.models import WarrantySale


class WarrantyForm(forms.ModelForm):
    class Meta:
        model = WarrantySale
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Nombre de la garantía'
            }),
            'description' : forms.Textarea(attrs={
                'placeholder' : 'Descripción de la garantía',
                'rows' : 2
            }),
            'months_coverred' : forms.NumberInput(attrs={
                'min' : 1,
                'max' : 24,
                'value' : 1
            })
        }
    
    def save(self, commit = True):
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