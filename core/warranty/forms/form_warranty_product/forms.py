from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
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
                instance = form.save(commit=False)
                instance.save()
                if is_actual_state_autoreplication():
                    instance.save(using='mirror_database')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
