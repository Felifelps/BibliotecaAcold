from django import forms
from books.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'quantity', 'author', 'category', 'publisher', 'location', 'publication_date', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control', 'value': 0}
            ),
            'author': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'category': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'publisher': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'location': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'publication_date': forms.DateInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'title': 'Título',
            'quantity': 'Quantidade',
            'author': 'Autor',
            'category': 'Categoria',
            'publisher': 'Editora (opcional)',
            'location': 'Localização',
            'publication_date': 'Data de publicação (opcional)',
            'description': 'Descrição (opcional)'
        }
