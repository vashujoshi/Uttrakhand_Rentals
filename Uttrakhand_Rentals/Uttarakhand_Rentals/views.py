from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Welcome to Uttrakhand rentals")
   return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("Contact us at uttarakhandrentals.in")