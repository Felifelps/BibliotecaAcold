from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from locations.models import Location
from locations.forms import LocationForm


class LocationListView(ListView):

    model = Location
    template_name = 'locations_list.html'
    context_object_name = 'locations'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        if (name := self.request.GET.get('name')):
            queryset = queryset.filter(name__icontains=name)

        return queryset


class LocationCreateView(CreateView):

    model = Location
    template_name = 'locations_create.html'
    form_class = LocationForm
    success_url = reverse_lazy('list-locations')


class LocationDetailView(DetailView):

    model = Location
    template_name = 'locations_detail.html'
    context_object_name = 'location'


class LocationUpdateView(UpdateView):

    model = Location
    template_name = 'locations_update.html'
    form_class = LocationForm
    success_url = reverse_lazy('list-locations')


class LocationDeleteView(DeleteView):

    model = Location
    template_name = 'locations_delete.html'
    success_url = reverse_lazy('list-locations')
    context_object_name = 'location'
