from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.pokemonologia, name='Pokemonologia'),
    path('register/', views.register, name='register'),
]
