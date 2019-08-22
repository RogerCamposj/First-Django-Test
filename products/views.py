from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    # return HttpResponse('QUALÉ RAPAZIADA')
    return render(request, 'index.html')

def new(request):
    return HttpResponse('NOVIDADES LOGO MAIS EM RAPAZIADA')

