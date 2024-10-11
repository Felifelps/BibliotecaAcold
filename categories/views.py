from django.views.generic import (
    ListView,
    CreateView
)
from django.urls import reverse_lazy
from categories.models import Category
from categories.forms import CategoryForm


class CategoryListView(ListView):

    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):

    model = Category
    template_name = 'categories_create.html'
    context_object_name = 'categories'
    form_class = CategoryForm
    success_url = reverse_lazy('list-categories')
