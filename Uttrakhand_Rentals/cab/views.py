from django.shortcuts import render
from .models import car_options
# Create your views here.

def home(request):
    cabs= car_options.objects.all()
    return render(request, 'cab_home.html', {'cabs': cabs})

