from django import forms
from core.product.models import Product


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
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                instance.save(using='stock_product')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
