from django.db import models
from authors.models import Author
from categories.models import Category
from locations.models import Location
from publishers.models import Publisher


class Book(models.Model):

    title = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='categories'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='locations'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name='publishers',
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)
