from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
user = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # username = form.cleaned_data.get('username')
        u = authenticate(request, email=email, password=password)
        print('USER EMAILX: %s' % u)

        if u and u.is_active:
            print('USER EMAIL: %s' % u.email)

            login(request, u)
            return redirect('reminder:index')

    context = {
        'form': form
    }

    return render(request, 'user-login.html', context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        username = form.cleaned_data.get('username')

        if password == password2:
            if not user.objects.filter(email=email):
                new_user = user(email=email, username=username)
                new_user.set_password(password)
                new_user.save()

                return redirect('user:login')  # redirect to login page to login
            return HttpResponse('Email already exists')
        return HttpResponse('Passwords must be the same')

    context = {
        'form': form
    }

    return render(request, 'user-login.html', context)