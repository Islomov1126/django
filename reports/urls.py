from django.urls import path, include
from .views import form6


urlpatterns = [
    path('form6', form6, name='form6')
]