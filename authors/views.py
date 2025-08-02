from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from authors.models import Author
from authors.forms import AuthorForm


class AuthorListView(LoginRequiredMixin, ListView):

    model = Author
    template_name = 'authors_list.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('created_at')

        if (name := self.request.GET.get('name')):
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AuthorCreateView(LoginRequiredMixin, CreateView):

    model = Author
    template_name = 'authors_create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('list-authors')


class AuthorDetailView(LoginRequiredMixin, DetailView):

    model = Author
    template_name = 'authors_detail.html'
    context_object_name = 'author'


class AuthorUpdateView(LoginRequiredMixin, UpdateView):

    model = Author
    template_name = 'authors_update.html'
    form_class = AuthorForm
    success_url = reverse_lazy('list-authors')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):

    model = Author
    template_name = 'authors_delete.html'
    success_url = reverse_lazy('list-authors')
    context_object_name = 'author'
