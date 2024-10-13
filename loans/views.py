from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from books.models import Book
from loans.models import Loan
from loans.forms import LoanForm
from readers.models import Reader


class LoanListView(ListView):

    model = Loan
    template_name = 'loans_list.html'
    context_object_name = 'loans'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if (book := self.request.GET.get('book')):
            queryset = queryset.filter(book__title__icontains=book)

        if (reader := self.request.GET.get('reader')):
            queryset = queryset.filter(reader__title__icontains=reader)

        return queryset


class LoanCreateView(CreateView):

    model = Loan
    template_name = 'loans_create.html'
    form_class = LoanForm
    success_url = reverse_lazy('list-loans')


class LoanDetailView(DetailView):

    model = Loan
    template_name = 'loans_detail.html'
    context_object_name = 'loan'


class LoanUpdateView(UpdateView):

    model = Loan
    template_name = 'loans_update.html'
    form_class = LoanForm
    success_url = reverse_lazy('list-loans')


class LoanDeleteView(DeleteView):

    model = Loan
    template_name = 'loans_delete.html'
    success_url = reverse_lazy('list-loans')
    context_object_name = 'loan'
