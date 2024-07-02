from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rating', views.rating, name='rating'),
    path('about', views.about, name='about'),
    path('receiving', views.receiving, name='receiving'),
    path('sending', views.sending, name='sending'),
]
