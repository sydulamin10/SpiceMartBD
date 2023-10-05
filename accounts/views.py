from django.shortcuts import render


# Create your views here.
def forget_pass(r):
    return render(r, 'accounts/Forget_password.html')


def signup(r):
    return render(r, 'accounts/Sign Up.html')


def signin(r):
    return render(r, 'accounts/Sign In.html')
