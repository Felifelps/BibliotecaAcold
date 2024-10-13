from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReaderListView.as_view(), name='list-readers'),
    path('create/', views.ReaderCreateView.as_view(), name='create-readers'),
    path('<int:pk>/', views.ReaderDetailView.as_view(), name='detail-readers'),
    path('<int:pk>/update', views.ReaderUpdateView.as_view(), name='update-readers'),
    path('<int:pk>/delete', views.ReaderDeleteView.as_view(), name='delete-readers'),
]
