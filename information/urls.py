from django.urls import path

from . import views

app_name = 'information'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>/', views.index, name='index'),
]

