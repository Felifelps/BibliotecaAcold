from django.urls import path
from . import views


urlpatterns = [
    path('', views.AuthorListView.as_view(), name='list-authors'),
    path('create/', views.AuthorCreateView.as_view(), name='create-authors'),
    path('<int:pk>/', views.AuthorDetailView.as_view(), name='detail-authors'),
    path('<int:pk>/update', views.AuthorUpdateView.as_view(), name='update-authors'),
    path('<int:pk>/delete', views.AuthorDeleteView.as_view(), name='delete-authors'),
]
