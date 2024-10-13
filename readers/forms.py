from django import forms
from readers.models import Reader


class ReaderForm(forms.ModelForm):

    class Meta:
        model = Reader
        fields = ['name', 'address', 'phone']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'phone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        labels = {
            'name': 'Nome',
            'address': 'Endereço',
            'phone': 'Telefone'
        }
