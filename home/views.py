from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
    DetailView,
    ListView)

def index(request):
    context = {}
    return render(request, 'home.html', context=context)
