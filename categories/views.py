from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from categories.models import Category
from categories.forms import CategoryForm


class CategoryListView(ListView):

    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()

        if (name := self.request.GET.get('name')):
            queryset = queryset.filter(name__icontains=name)

        if (cdd := self.request.GET.get('cdd')):
            queryset = queryset.filter(cdd__icontains=cdd)

        return queryset


class CategoryCreateView(CreateView):

    model = Category
    template_name = 'categories_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('list-categories')


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'categories_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):

    model = Category
    template_name = 'categories_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('list-categories')


class CategoryDeleteView(DeleteView):

    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('list-categories')
    context_object_name = 'category'
