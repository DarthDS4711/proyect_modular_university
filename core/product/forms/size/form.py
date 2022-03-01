from django import forms

from core.product.models import Size


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        widgets = {
            'size_product' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese el nombre de la medida'
            })
        }