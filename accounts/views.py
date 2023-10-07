from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def forget_pass(r):
    return render(r, 'accounts/Forget_password.html')


def signup(r):
    if r.user.is_authenticated:
        return redirect('home')

    if r.method == 'POST':
        first_name = r.POST.get('first_name')
        last_name = r.POST.get('last_name')
        username = r.POST.get('username')
        email = r.POST.get('email')
        password = r.POST.get('pass')
        password1 = r.POST.get('pass1')
        if len(password) < 8:
            messages.success(r, "Profile pass must be 8 character.")
        else:
            if password:
                a = []
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c = []
                d = ['&', '$', '#', '@', '*', '!', '_', '/', '-']
                for i in b:
                    if i in password:
                        a.append(i)
                for i in d:
                    if i in password:
                        c.append(i)

                if len(a) != 0 and len(c) != 0:
                    if password == password1:
                        if User.objects.filter(username=username).exists():
                            messages.success(r, "Profile Name Already Taken.")
                        elif User.objects.filter(email=email).exists():
                            messages.success(r, "Profile Email Already Taken.")
                        else:
                            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                            username=username, password=password)
                            user.set_password(password)
                            user.save()
                            messages.success(r, "Profile Created.")
                            return redirect('signin')
                    else:
                        messages.warning(r, "Profile Password not Matched.")
                else:
                    messages.warning(r, "enter minimum 1 number and 1 special character in your password.")

    return render(r, 'accounts/Sign Up.html')


def signin(r):
    if r.user.is_authenticated:
        return redirect('home')

    if r.method == 'POST':
        username = r.POST.get('name')
        password = r.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(r, user)
            messages.warning(r, "User Logged in.")
            return redirect('home')
        else:
            messages.warning(r, "User Not Found.")
            return redirect('signup')
    return render(r, 'accounts/Sign In.html')


def signout(r):
    auth.logout(r)
    return redirect('signin')
