from django.shortcuts import render, HttpResponse, redirect
from .models import Products, Categories
from random import randint
from datetime import datetime

def index(request):
    produtos = Products.objects.filter(in_stock=True)
    return render(request, 'pages/index.html', {'produtos': produtos})

def out_of_stock(request):
    produtos = Products.objects.filter(in_stock=False)
    return render(request, 'pages/index.html', {'produtos': produtos})

def search_product(request):
    q = request.GET.get('q')
    produtos = Products.objects.filter(name__icontains=q)
    return render (request, 'pages/index.html', {'produtos':produtos}) 

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cod = randint(100, 10000)
        category = request.POST.get('category')
        picture = request.FILES.get('picture')
        price = request.POST.get('price')
        description = request.POST.get('description')
        qtd = request.POST.get('qtd')
        discount = request.POST.get('discount')
        created_at = datetime.now()
        in_stock = True

    
        Products.objects.create(
            name=name,cod=cod,category_id=category,
            picture=picture, price=price, description=description,
            qtd=qtd,discount=discount,created_at=created_at,in_stock=in_stock
        )
        return redirect('home')
    else:
        categories = Categories.objects.all()
        return render(request, 'pages/add-product.html', {'categories':categories})


def product_details(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product_details.html', {'product':product})

def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('home')

def sell_product(request, id):
    product = Products.objects.get(id=id)
    product.qtd -= 1
    if product.qtd == 0:
        product.in_stock = False
    product.save()
    return redirect('product-details', id)