from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.product.models import Product
from core.supplier.models import Supplier


# formulario Django para el producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'supplier_id','size', 'pvp', 'image', 'discount', 
            'description', 'primary_color', 'secondary_color', 'last_color',  'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nombre producto'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Descripción del producto'
            }),
            'primary_color' : forms.TextInput(attrs={
                'type' : 'color'
            }),
            'secondary_color' : forms.TextInput(attrs={
                'type' : 'color'
            }),
            'last_color' : forms.TextInput(attrs={
                'type' : 'color'
            }),
            'supplier_id' : forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
            })
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                instance.save(using='stock_product')
                if is_actual_state_autoreplication():
                    instance.save(using='mirror_database')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        print(data)
        return data
