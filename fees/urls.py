from django.urls import path

from . import views

app_name = 'fees'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_init, name='search'),
    path('update/', views.update_init, name='update'),
    path('total/', views.total_init, name='total'),
]

