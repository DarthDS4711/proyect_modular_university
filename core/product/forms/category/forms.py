from django import forms
from core.product.models import Category


# formulario Django para la categoria
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nombre categoria'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Descripción de la categoría'
            }),
        }

    # sobreescritura del método save para guardar en bases 
    # de datos distribuidas
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
