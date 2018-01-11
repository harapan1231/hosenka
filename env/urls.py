from django.urls import path

from . import views

app_name = 'env'
urlpatterns = [
    path('', views.index, name='index'),
]

