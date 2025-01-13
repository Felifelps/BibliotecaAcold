from datetime import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from categories.models import Category


def home(request):
    url = 'list-loans' if request.user.is_authenticated else 'login'
    return HttpResponseRedirect(reverse(url))


def activate_db(request):
    try:
        count = Category.objects.count()
        content = f"Activated succesfully ({count})!"
    except Exception as e:
        content = f"An error ocurred ({datetime.now()})"
    return HttpResponse(content=content)
