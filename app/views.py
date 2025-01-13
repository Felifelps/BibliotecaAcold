from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from categories.models import Category


def home(request):
    url = 'list-loans' if request.user.is_authenticated else 'login'
    return HttpResponseRedirect(reverse(url))


def activate_db(request):
    count = Category.objects.count()
    return HttpResponse(
        content=f"Activated succesfully ({count})!"
    )
