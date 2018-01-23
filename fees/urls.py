from django.urls import path

from . import views

app_name = 'total'
urlpatterns = [
    path('', views.index, name='index'),
    path('total/', views.total, name='total'),
]

