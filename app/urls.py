from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # dashboard path('/', ...),
    path('authors/', include('authors.urls')),
    path('books/', include('books.urls')),
    path('categories/', include('categories.urls')),
    path('loans/', include('loans.urls')),
    path('locations/', include('locations.urls')),
    path('readers/', include('readers.urls')),
]
