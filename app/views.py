from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    url = 'list-loans' if request.user.is_authenticated else 'login'
    return HttpResponseRedirect(reverse(url))
