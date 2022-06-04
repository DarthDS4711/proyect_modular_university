from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.stock.models import Stock


# formulario Django para registrar un stock
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ['amount']

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
        return data


# formulario para editar un stock
class StockEditForm(forms.ModelForm):
    class Meta:
        model = Stock
        # exclude es para quitar un campo de nuestro formulario
        exclude = ['product', 'amount']
    
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
        return data

