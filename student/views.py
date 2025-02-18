from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def products(request):
    prods = Product.objects.all()
    return render(request,"templates_student/products.html", {"products": prods})