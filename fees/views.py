from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Ret

def index(request):
    template = loader.get_template('fees/index.html')
    context = {
        'title': 'Home',
        'ret': Ret.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('fees/search.html')
    context = {
        'title': 'Search',
        'ret': Ret.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def update(request):
    template = loader.get_template('fees/update.html')
    context = {
        'title': 'Update',
    }
    return HttpResponse(template.render(context, request))

def total(request):
    template = loader.get_template('fees/total.html')
    context = {
        'title': 'Total',
    }
    return HttpResponse(template.render(context, request))

