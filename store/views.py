from django.shortcuts import render
from .models import Category, Product

from core import settings


def all_products(request):
    products = Product.objects.all()
    category = Product.objects.filter(in_stock=True).select_related('category')
    context = {'products': products, 'category':category}
    return render(request, 'store/home.html', context)

