from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Welcome to Uttrakhand rentals")
   return render(request, 'home.html')
def about(request):
    return HttpResponse("Uttrakhand rental is the best service for booking stays in uttrakhand")

def contact(request):
    return HttpResponse("Contact us at uttrakhandrentals.in")