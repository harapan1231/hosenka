from django.urls import path

from . import views

app_name = 'tally'
urlpatterns = [
    path('', views.index, name='index'),
]

