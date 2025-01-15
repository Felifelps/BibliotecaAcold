from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from publishers.models import Publisher
from publishers.forms import PublisherForm


class PublisherListView(LoginRequiredMixin, ListView):

    model = Publisher
    template_name = 'publishers_list.html'
    context_object_name = 'publishers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('created_at')

        if (name := self.request.GET.get('name')):
            queryset = queryset.filter(name__icontains=name)

        return queryset


class PublisherCreateView(LoginRequiredMixin, CreateView):

    model = Publisher
    template_name = 'publishers_create.html'
    form_class = PublisherForm
    success_url = reverse_lazy('list-publishers')


class PublisherDetailView(LoginRequiredMixin, DetailView):

    model = Publisher
    template_name = 'publishers_detail.html'
    context_object_name = 'publisher'


class PublisherUpdateView(LoginRequiredMixin, UpdateView):

    model = Publisher
    template_name = 'publishers_update.html'
    form_class = PublisherForm
    success_url = reverse_lazy('list-publishers')


class PublisherDeleteView(LoginRequiredMixin, DeleteView):

    model = Publisher
    template_name = 'publishers_delete.html'
    success_url = reverse_lazy('list-publishers')
    context_object_name = 'publisher'
