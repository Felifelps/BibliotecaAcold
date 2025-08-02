from django import forms
from authors.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição (opcional)'
        }
