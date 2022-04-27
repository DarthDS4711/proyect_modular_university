from django import forms
from core.warranty.models import WarrantyProduct


class WarrantyProductForm(forms.ModelForm):
    class Meta:
        model = WarrantyProduct
        fields = '__all__'
        widgets = {
            'product' : forms.Select(attrs={
                'class' : 'form-control'
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
