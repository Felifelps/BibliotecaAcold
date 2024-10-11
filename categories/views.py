from django.views.generic import (
    ListView,
    CreateView
)
from categories.models import Category


class CategoryListView(ListView):

    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):

    model = Category
    template_name = 'categories_create.html'
    context_object_name = 'categories'
