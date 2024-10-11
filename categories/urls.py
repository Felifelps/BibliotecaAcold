from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='list-categories'),
    #path('create/', ..., name='create-categories'),
    #path('<int:pk>/', ..., name='detail-categories'),
    #path('<int:pk>/update', ..., name='update-categories'),
    #path('<int:pk>/delete', ..., name='delete-categories'),
]
