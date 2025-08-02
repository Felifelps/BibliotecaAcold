from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoanListView.as_view(), name='list-loans'),
    path('create/', views.LoanCreateView.as_view(), name='create-loans'),
    path('<int:pk>/', views.LoanDetailView.as_view(), name='detail-loans'),
    path('<int:pk>/update', views.LoanUpdateView.as_view(), name='update-loans'),
    path('<int:pk>/delete', views.LoanDeleteView.as_view(), name='delete-loans'),
]
