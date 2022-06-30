from django.shortcuts import render
from .models import Category
# Create your views here.
def index(request):
    objects = Category.objects.all()
    print(objects)
    context ={'objects':objects}
    return render(request=request, template_name='main/index.html', context=context)
