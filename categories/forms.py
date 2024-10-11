from django import forms
from categories.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['cdd', 'description']
        widgets = {
            'cdd': forms.NumberInput(
                attrs={'class': 'form-control', 'step': 'any'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'cdd': 'CDD',
            'description': 'Descrição'
        }