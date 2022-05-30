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
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance_save =  form.save(commit=False)
                instance_save.save()
                instance_save.save(using='stock_product')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data