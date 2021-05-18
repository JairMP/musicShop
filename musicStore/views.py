from products.models import Product
from django.contrib import auth
from django.contrib.messages.api import success
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm

#from django.contrib.auth.models import User
from users.models import User



def index(request):

    products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'products': products
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('index')
        else:
            messages.error(request, 'Hubo un Error')

    return render(request, 'users/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion Cerrada')
    return redirect('login')


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()

        if user:
            login(request, user)
            messages, success(request, 'Usuario Creado Exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })
