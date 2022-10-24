from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import RegistrationForm, AuthorizationForm


def registration(request):
    is_authenticated = request.user.is_authenticated
    is_admin = request.user.is_staff
    form = RegistrationForm()

    context = {
        'is_authenticated': is_authenticated,
        'is_admin': is_admin,
        'form': form,
    }

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

        user = User.objects.create_user(login, email, password)
        user.save()
        login(request, user)
        return redirect(reverse('newsboard'))

    return render(request, 'registration/reg.html', context)


def authorization(request):
    is_authenticated = request.user.is_authenticated
    is_admin = request.user.is_staff
    form = AuthorizationForm()
    error = ''

    context = {
        'is_authenticated': is_authenticated,
        'is_admin': is_admin,
        'form': form,
        'error': error,
    }

    if request.POST:
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user != None:
                login(request, user)
                return redirect(reverse('newsboard'))

            else:
                error = 'Wrong password'

    return render(request, 'authorisation/auth.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('newsboard'))
