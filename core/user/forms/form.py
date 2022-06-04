from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.product.models import Product
from core.user.models import DirectionUser

# formulario para registrar las direcciones del usuario
class DirectionUserForm(forms.ModelForm):
    class Meta:
        model = DirectionUser
        exclude = ('user',)
        widgets = {
            'interior_number' : forms.TextInput(attrs={
                'required' : False
            })
        }
    

    def save(self, commit=True):
        # json a regresar en caso de errores al guardar
        data = {}
        # obtención del formulario
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

