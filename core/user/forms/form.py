from django import forms
from core.product.models import Product
from core.user.models import DirectionUser

# formulario para registrar las direcciones del usuario
class DirectionUserForm(forms.ModelForm):
    class Meta:
        model = DirectionUser
        fields = ['direction', 'is_active']
        widgets = {
            'direction' : forms.TextInput(attrs={
                'placeholder' : 'Dirección completa del lugar'
            })
        }
    

    def save(self, commit=True):
        # json a regresar en caso de errores al guardar
        data = {}
        # obtención del formulario
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

