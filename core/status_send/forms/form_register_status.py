from django import forms
from core.status_send.models import StatusSend


class StatusSendForm(forms.ModelForm):
    
    class Meta:
        model = StatusSend
        fields = '__all__'
        widgets = {
            'description' : forms.TextInput(attrs={
                'placeholder' : 'Ingrese el nombre del estado'
            })
        }
    def save(self, commit=True):
        data = {}
        form = super()
        print(form)
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data