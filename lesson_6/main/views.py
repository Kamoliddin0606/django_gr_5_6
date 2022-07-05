from django.shortcuts import render
from .models import Category, Product
# Create your views here.
def index(request, id=None):
    objects = Category.objects.all()

    if  id==None:
        products = Product.objects.all()

    else:  
        objectcat = Category.objects.get(id=id)
        products = Product.objects.filter(category=objectcat)

    print(products.query)
    context ={'objects':objects, 'products':products}
    return render(request=request, template_name='main/index.html', context=context)
