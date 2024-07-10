from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('rating/', views.rating, name='rating'),
    path('profile/', views.profile, name='profile'),
    path('receiving/', views.receiving, name='receiving'),
    path('sending/', views.sending, name='sending'),
    path('receiving/<int:level>/', views.receiving_level, name='receiving_level'),
    path('receiving/<int:level>/reset', views.reset_receiving_level, name='reset_receiving_level'),
    path('sending/<int:level>/', views.sending_level, name='sending_level'),
    path('sending/<int:level>/reset', views.reset_sending_level, name='reset_sending_level'),
    path('translator/', views.translator, name='translator'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
]
