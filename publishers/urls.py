from django.urls import path
from . import views


urlpatterns = [
    path('', views.PublisherListView.as_view(), name='list-publishers'),
    path('create/', views.PublisherCreateView.as_view(), name='create-publishers'),
    path('<int:pk>/', views.PublisherDetailView.as_view(), name='detail-publishers'),
    path('<int:pk>/update', views.PublisherUpdateView.as_view(), name='update-publishers'),
    path('<int:pk>/delete', views.PublisherDeleteView.as_view(), name='delete-publishers'),
]
