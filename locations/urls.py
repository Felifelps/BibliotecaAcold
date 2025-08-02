from django.urls import path
from . import views


urlpatterns = [
    path('', views.LocationListView.as_view(), name='list-locations'),
    path('create/', views.LocationCreateView.as_view(), name='create-locations'),
    path('<int:pk>/', views.LocationDetailView.as_view(), name='detail-locations'),
    path('<int:pk>/update', views.LocationUpdateView.as_view(), name='update-locations'),
    path('<int:pk>/delete', views.LocationDeleteView.as_view(), name='delete-locations'),
]
