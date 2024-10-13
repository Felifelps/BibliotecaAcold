from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from authors.models import Author
from books.models import Book
from books.forms import BookForm
from categories.models import Category
from locations.models import Location


class BookListView(ListView):

    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if (title := self.request.GET.get('title')):
            queryset = queryset.filter(title__icontains=title)

        if (author := self.request.GET.get('author')):
            queryset = queryset.filter(author__name__icontains=author)

        if (category := self.request.GET.get('category')):
            queryset = queryset.filter(category__name__icontains=category)

        if (location := self.request.GET.get('location')):
            queryset = queryset.filter(location__name__icontains=location)

        return queryset


class BookCreateView(CreateView):

    model = Book
    template_name = 'books_create.html'
    form_class = BookForm
    success_url = reverse_lazy('list-books')


class BookDetailView(DetailView):

    model = Book
    template_name = 'books_detail.html'
    context_object_name = 'book'


class BookUpdateView(UpdateView):

    model = Book
    template_name = 'books_update.html'
    form_class = BookForm
    success_url = reverse_lazy('list-books')


class BookDeleteView(DeleteView):

    model = Book
    template_name = 'books_delete.html'
    success_url = reverse_lazy('list-books')
    context_object_name = 'book'
