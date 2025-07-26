from django.urls import path
from .views import calculadora_view

urlpatterns = [
    path('', calculadora_view, name='calculadora'),
]
