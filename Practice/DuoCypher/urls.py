from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rating', views.rating, name='rating'),
    path('profile', views.profile, name='profile'),
    path('receiving', views.receiving, name='receiving'),
    path('sending', views.sending, name='sending'),
    path('receiving/<int:level>/', views.receiving_level, name='receiving_level'),
    path('sending/<int:level>/', views.sending_level, name='sending_level'),
    path('translator/', views.translator, name='translator'),
]
