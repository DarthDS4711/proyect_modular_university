from django import forms
from core.user.models import User


# formulario del reseteo de la contraseña ingresando el username
class UserResetPwdForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ingresa el username'
                })
        }
    
    
