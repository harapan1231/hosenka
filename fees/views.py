from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world.")

def total(request):
    template = loader.get_template('fees/total.html')
    context = {
        'title': 'Total',
    }
    return HttpResponse(template.render(context, request))

