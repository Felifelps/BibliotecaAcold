from django import forms
from books.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'location', 'publication_date', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'author': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'category': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'location': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'publication_date': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
        labels = {
            'title': 'Nome',
            'author': 'Autor',
            'category': 'Categoria',
            'location': 'Localização',
            'publication_date': 'Data de publicação (opcional)',
            'description': 'Descrição (opcional)'
        }
