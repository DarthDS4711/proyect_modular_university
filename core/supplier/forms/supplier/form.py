from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
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
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance_save =  form.save(commit=False)
                instance_save.save()
                instance_save.save(using='stock_product')
                if is_actual_state_autoreplication():
                    instance_save.save(using='mirror_database')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data