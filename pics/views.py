from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image, Category, Location

# Create your views here.
def welcome(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html',{"categories":categories,"locations":locations})