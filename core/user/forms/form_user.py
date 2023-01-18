from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.user.models import User
from django.db import transaction


class UserEditForm(forms.ModelForm):
    date_birthday = forms.DateField(
            widget=forms.DateInput(format=('%d-%m-%Y'),
            attrs={
                'class': 'datepicker', 
                'placeholder': 
                'Select a date', 
                'type': 'date'
            }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
            'image', 'date_birthday', 'gender']
        
    
    #sobreescritura del método save para mandar al front-end los datos de estado del registro
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                u = form.save(commit=False)
                u.save()
                if is_actual_state_autoreplication():
                    u.save(using = 'mirror_database')
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
