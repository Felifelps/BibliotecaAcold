from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # dashboard path('/', ...),
    path('categories/', include('categories.urls')),
    # path('books/', include('books.urls')),
    # path('users/', include('users.urls')),
    # path('loans/', include('loans.urls')),
    # path('locations/', include('locations.urls')),
]
