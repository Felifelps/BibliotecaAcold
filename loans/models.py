from django.db import models
from books.models import Book
from readers.models import Reader


class Loan(models.Model):

    loan_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='loans'
    )
    reader = models.ForeignKey(
        Reader,
        on_delete=models.PROTECT,
        related_name='loans'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.loan_date)
