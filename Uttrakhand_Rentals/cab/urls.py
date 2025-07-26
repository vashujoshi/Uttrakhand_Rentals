

from django.urls import path
from . import  views

# localhost:8000:cab
urlpatterns = [
  path('', views.home, name='home'),
  
] 