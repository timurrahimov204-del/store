from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   
from orders.models import Order



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:profile_view')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login_view')


def profile_view(request):
    return render(request, 'registration:profile')


@login_required(login_url='accounts:login_view')
def profile_view(request):
    active_orders = Order.objects.filter(user=request.user, status='active')
    canceled_orders = Order.objects.filter(user=request.user, status='canceled')
    completed_orders = Order.objects.filter(user=request.user, status='completed')
    return render(request, 'registration/profile.html', {'active_orders':active_orders,
                                                         'canceled_orders':canceled_orders,
                                                         'completed_orders':completed_orders})

def all_orders(request):
    order_user = Order.user
    return render(request, 'registration/all_orders.html', {'all_orders':order_user})







