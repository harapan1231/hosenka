from django.urls import path

from . import views

app_name = 'fees'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('update/', views.update, name='update'),
    path('total/', views.total, name='total'),
]

