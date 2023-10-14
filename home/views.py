from django.shortcuts import render
from products.models import *


# Create your views here.
def home(request):
    cata = category.objects.all()
    return render(request, 'home/home.html', locals())
