from django import forms
from locations.models import Location


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
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
