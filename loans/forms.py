from django import forms
from loans.models import Loan


class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = [
            'book',
            'reader',
            'loan_date',
            'expected_return_date',
            'actual_return_date',
            'returned',
        ]
        widgets = {
            'book': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'reader': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'loan_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'expected_return_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'actual_return_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'returned': forms.CheckboxInput(
                check_test=lambda value: value,
                attrs={
                    'type': 'checkbox',
                }
            ),
        }
        labels = {
            'book': 'Livro',
            'reader': 'Leitor',
            'loan_date': 'Data empréstimo',
            'expected_return_date': 'Data de devolução prevista',
            'actual_return_date': 'Data de devolução real (opcional)',
            'returned': 'Livro devolvido',
        }
