from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Gartllery'
    return render(request, 'index.html',{'images':images,'locations':locations,'categories':categories, 'title':title})