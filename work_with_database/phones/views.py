from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all
    name = request.GET.get('name')
    price = request.GET.get('price')
    if Phone.objects.price["min_price"]:
       phones = Phone.objects.filter(price__gte=Phone.objects.price["min_price"])
    if Phone.objects.price["max_price"]:
       phones = Phone.objects.filter(price__lte=Phone.objects.price["max_price"])
    if Phone.objects.name("name"):
       phones = Phone.objects.filter(name=Phone.objects.name("name"))
    context = {'phones': phones_all,
                'name': name,
                'price': price,}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug__contains=slug).first()
    context = {'phones': phones,}
    return render(request, template, context)

