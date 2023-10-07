from django.urls import path
from .views import forget_pass, signup, signin, signout

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('forget_pass/', forget_pass, name='forget_pass'),
]
