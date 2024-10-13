from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # dashboard path('/', ...),
    path('categories/', include('categories.urls')),
    path('readers/', include('readers.urls')),
    # path('books/', include('books.urls')),
    # path('loans/', include('loans.urls')),
    # path('locations/', include('locations.urls')),
]
