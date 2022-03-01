from django import forms
from core.product.models import Category


# formulario Django para la categoria
class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
		widgets = {
			'name' : forms.TextInput(attrs={
				'placeholder' : 'Nombre categoria'
			}),
			'description' : forms.TextInput(attrs={
				'placeholder' : 'Descripción de la categoría'
			}),
			'name' : forms.TextInput(attrs={
				'placeholder' : 'Nombre categoria'
			}),
		}