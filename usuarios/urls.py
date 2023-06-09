from django.urls import path
from . import views

urlpatterns = [
    path('autenticacao/', views.autenticacao, name='autenticacao'),
    path('', views.plataforma, name="plataforma")
]