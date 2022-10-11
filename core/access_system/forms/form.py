from django import forms
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.user.models import User
from django.contrib.auth.models import Group


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
                # obtenemos la contraseña del usuario
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                # guardamos el usuario y verificamos que exista
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                # obtenemos la contraseña, la encriptamos y la guardamos
                u.save()
                client_group = Group.objects.get(name = 'Client')
                u.groups.add(client_group)
                if is_actual_state_autoreplication():
                    u.save(using = 'mirror_database')
                # asignamos un grupo por defecto en los usuarios
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
