from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('results/', views.results, name = 'results'),
    path('aboutus/', views.aboutus, name = 'aboutus')
]