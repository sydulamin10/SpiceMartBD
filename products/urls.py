from django.urls import path
from .views import *

urlpatterns = [
    path('product/<int:id>/', product, name='product'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
]
