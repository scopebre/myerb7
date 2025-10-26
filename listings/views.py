from django.shortcuts import render
from .models import Listing

# Create your views here.
def listings(request):
    listings = Listing.objects.all()
    context = {"listing":listings}
    return render(request,'listings/listings.html')
def listing(request):
    return render(request,'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')