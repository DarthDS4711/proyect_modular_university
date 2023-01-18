from django import forms


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese la nueva contraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirma la nueva contraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

