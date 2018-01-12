from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request, title = ''):
    template = loader.get_template('information/index.html')
    context = {
        'title': title if title else 'Information',
    }
    return HttpResponse(template.render(context, request))

