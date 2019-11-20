from django.shortcuts import render


from .models import Category
from .models import Product
# Create your views here.

def category(request):
    category = Category.objects.all()


def product(request):
    product = Product.objects.all()

