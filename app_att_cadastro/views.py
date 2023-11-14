from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .services.api_ibge import Regioes

def login_page(request):
    return render(request, 'login/index.html')


def logar(request):
    user = authenticate(username=request.POST.get('username'),
                        password=request.POST.get('password'))
    if user is not None:
        login(request,user)
        return redirect(home)
    return redirect(login_page)

def deslogar(request):
    logout(request)
    return redirect(login_page)

@login_required
def home(request):
    user = User.objects.get(username=request.user)
    if user.is_staff or user.is_superuser:
        return render(request, 'home/staff.html')
    regioes = Regioes()
    ufs = []
    for uf in regioes.uf:
        ufs.append(uf['nome'])
    print(ufs)
    dados = {
        'ufs': sorted(ufs),
        'cidades': regioes.cidades
    }

    return render(request, 'home/user.html', dados)
