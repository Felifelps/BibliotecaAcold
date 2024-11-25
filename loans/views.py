from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from loans.models import Loan
from loans.forms import LoanForm


class LoanListView(LoginRequiredMixin, ListView):

    model = Loan
    template_name = 'loans_list.html'
    context_object_name = 'loans'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('created_at')

        if (book := self.request.GET.get('book')):
            queryset = queryset.filter(book__title__icontains=book)

        if (reader := self.request.GET.get('reader')):
            queryset = queryset.filter(reader__name__icontains=reader)

        if (loan_date := self.request.GET.get('loan_date')):
            loan_date = date.fromisoformat(loan_date)
            queryset = queryset.filter(loan_date=loan_date)

        if (was_returned := self.request.GET.get('was_returned')):
            queryset = queryset.filter(returned=was_returned == '1')

        return queryset


class LoanCreateView(LoginRequiredMixin, CreateView):

    model = Loan
    template_name = 'loans_create.html'
    form_class = LoanForm
    success_url = reverse_lazy('list-loans')


class LoanDetailView(LoginRequiredMixin, DetailView):

    model = Loan
    template_name = 'loans_detail.html'
    context_object_name = 'loan'


class LoanUpdateView(LoginRequiredMixin, UpdateView):

    model = Loan
    template_name = 'loans_update.html'
    form_class = LoanForm
    success_url = reverse_lazy('list-loans')


class LoanDeleteView(LoginRequiredMixin, DeleteView):

    model = Loan
    template_name = 'loans_delete.html'
    success_url = reverse_lazy('list-loans')
    context_object_name = 'loan'
