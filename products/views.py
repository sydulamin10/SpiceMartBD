from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect


# Create your views here.

def product(request, id):
    cat = category.objects.get(id=id)
    prod = product_all.objects.filter(category=cat)
    return render(request, 'product/product.html', locals())


def add_to_cart(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        try:
            pro = cart.objects.filter(product=prod)
            if pro:
                for i in pro:
                    i.quantity += 1
                    i.save()
                    return redirect(request.META['HTTP_REFERER'])
            else:
                crt = cart.objects.create(
                    user=user,
                    product=prod
                )
                crt.save()
                return redirect(request.META['HTTP_REFERER'])
        except Exception as e:
            print(e)

