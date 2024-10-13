from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='list-books'),
    path('create/', views.BookCreateView.as_view(), name='create-books'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail-books'),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name='update-books'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='delete-books'),
]
