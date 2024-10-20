from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from users.forms import UserRegisterForm, UserLoginForm


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'users/register.html', {'form': UserRegisterForm})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('app:index'))  # вместо app имя вашего приложения
                else:
                    return HttpResponse('Аккаунт неактивен!')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})
