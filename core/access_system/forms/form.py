from django import forms
from core.user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
            'password', 'image', 'date_birthday', 'gender']
        
        widgets = {
            'password' : forms.PasswordInput(),
            'date_birthday' : forms.DateInput()
        }
    
    #sobreescritura del método save para mandar al front-end los datos de estado del registro
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