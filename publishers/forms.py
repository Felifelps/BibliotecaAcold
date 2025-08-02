from django import forms
from publishers.models import Publisher


class PublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
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
