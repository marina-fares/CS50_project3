from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/orders/profile')
    else:
        form = UserRegisterForm()
    context={
        'form': form,
    }
    return render(request, 'register.html', context) 

