from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

