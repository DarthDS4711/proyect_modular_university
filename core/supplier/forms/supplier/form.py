from django import forms
from core.supplier.models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese el nombre del proveedor'
            }),
            'last_names' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese los apellidos del proveedor'
            }),
            'telephone' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese el telefono del proveedor'
            })
        }