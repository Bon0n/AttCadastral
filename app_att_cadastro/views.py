from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .services.ajax import is_ajax
from .services.api_ibge import Regioes
from .services.api_cep import buscar_cep


def login_page(request):
    return render(request, 'login/index.html')


def logar(request):
    user = authenticate(username=request.POST.get('username'),
                        password=request.POST.get('password'))
    if user is not None:
        login(request, user)
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
    dados = {
        'ufs': sorted(regioes.uf, key=lambda i: i['nome']),
    }

    return render(request, 'home/user.html', dados)


def pegar_cidade(request, uf):
    if is_ajax(request):
        regioes = Regioes()
        cidade = regioes.pegar_cidades(uf)
        return JsonResponse({'data': list(cidade)})
    return JsonResponse({'data': ''})


def busca_cep(request, cep):
    if is_ajax(request):
        data = {'data': buscar_cep(cep)}
        print(data['data']['cep'])
        return JsonResponse({'data': buscar_cep(cep)})
    return JsonResponse({'data': ''})
