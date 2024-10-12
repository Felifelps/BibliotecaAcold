from django import forms
from categories.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'cdd', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'cdd': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'name': 'Nome',
            'cdd': 'CDD (opcional)',
            'description': 'Descrição (opcional)'
        }
