from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import SearchResult

def index(request):
    template = loader.get_template('fees/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('fees/search.html')
    context = {
        'title': 'Search',
        'ret': SearchResult.objects.all(),
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

