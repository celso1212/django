from django.shortcuts import render, HttpResponse
from .models import Products

def index(request):
    produtos = Products.objects.all()
    for produto in produtos:
        print(produto.name)
    return render(request, 'pages/index.html', {'produtos':produtos})
