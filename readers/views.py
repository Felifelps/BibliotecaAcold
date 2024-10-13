from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from readers.models import Reader
from readers.forms import ReaderForm


class ReaderListView(ListView):

    model = Reader
    template_name = 'readers_list.html'
    context_object_name = 'readers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if (name := self.request.GET.get('name')):
            queryset = queryset.filter(name__icontains=name)

        if (address := self.request.GET.get('address')):
            queryset = queryset.filter(address__icontains=address)

        return queryset


class ReaderCreateView(CreateView):

    model = Reader
    template_name = 'readers_create.html'
    form_class = ReaderForm
    success_url = reverse_lazy('list-readers')


class ReaderDetailView(DetailView):

    model = Reader
    template_name = 'readers_detail.html'
    context_object_name = 'reader'


class ReaderUpdateView(UpdateView):

    model = Reader
    template_name = 'readers_update.html'
    form_class = ReaderForm
    success_url = reverse_lazy('list-readers')


class ReaderDeleteView(DeleteView):

    model = Reader
    template_name = 'readers_delete.html'
    success_url = reverse_lazy('list-readers')
    context_object_name = 'reader'
