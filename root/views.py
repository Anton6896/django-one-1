from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # log in user
            user = authenticate(username=username,
                                password=form.cleaned_data.get('password1'))
            if user:  # check the valid user before login
                if user.is_active:
                    login(request, user)

            messages.success(request, f'account created for {username}')
            return redirect('sales:home')
    else:
        form = UserRegisterForm()

    return render(request, 'root/register.html', {
        'form': form,
        'title': 'register'
    })
