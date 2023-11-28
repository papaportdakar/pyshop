from django.shortcuts import render
from .models import Products

# Create your views here.

def index(request):
	products = Products.objects.all()
	return render(request, 'index.html', {'products': products})



def new(request):
	return render(request, 'new.html')
