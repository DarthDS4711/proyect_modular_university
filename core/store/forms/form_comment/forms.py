from django import forms
from core.product.models import Comment


class CommentUserForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        widgets = {
            'description' : forms.Textarea(attrs={
                'placeholder' : 'Descripción de la valoración',
                'class' : 'form-control'
            })
        }
