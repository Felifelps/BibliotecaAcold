from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='list-categories'),
    path('create/', views.CategoryCreateView.as_view(), name='create-categories'),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name='detail-categories'),
    path('<int:pk>/update', views.CategoryUpdateView.as_view(), name='update-categories'),
    path('<int:pk>/delete', views.CategoryDeleteView.as_view(), name='delete-categories'),
]
