from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Funcionario
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
    regioes = Regioes()
    try:
        funcionario = Funcionario.objects.get(id_login=user.id)
        dados = {
            'ufs': sorted(regioes.uf, key=lambda i: i['nome']),
            'funcionario': funcionario,
        }
        if user.is_staff or user.is_superuser:
            return render(request, 'home/user.html', dados)
            #return render(request, 'home/staff.html')
        return render(request, 'home/user.html', dados)
    except:
        dados = {
            'ufs': sorted(regioes.uf, key=lambda i: i['nome']),
            'funcionario': '',
        }
    if user.is_staff or user.is_superuser:
        return render(request, 'home/user.html', dados)
        # return render(request, 'home/staff.html')
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


def salvar_dados(request):
    # Login
    id_login = User.objects.get(username=request.user)
    # Dados Pessoais
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cor = request.POST.get('cor')
    possui_filhos = request.POST.get('possui-filhos')
    genero = request.POST.get('genero')
    cpf = request.POST.get('cpf')
    estado_civil = request.POST.get('estado-civil')
    grau_escolaridade = request.POST.get('grau-escolaridade')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    bairro = request.POST.get('bairro')
    estado = request.POST.get('estado')
    cidade = request.POST.get('cidades')
    # Trabalho
    empresa = request.POST.get('empresa')
    email_corporativo = request.POST.get('email-corporativo')
    modelo_trabalho = request.POST.get('modelo-trabalho')
    gerente = request.POST.get('gerente')
    departamento = request.POST.get('departamento')
    cargo = request.POST.get('cargo')
    # Saude
    alergia = request.POST.get('alergia')
    tratamento_saude = request.POST.get('tratamento-saude')
    medicamento_continuo = request.POST.get('medicamento-continuo')
    # Contato
    telefonepessoal1 = request.POST.get('telefonepessoal1')
    telefonepessoal2 = request.POST.get('telefonepessoal2')
    nome_emergencia1 = request.POST.get('nome-emergencia1')
    telefone_emergencia1 = request.POST.get('telefone-emergencia1')
    grau_parentesco1 = request.POST.get('grau-parentesco1')
    nome_emergencia2 = request.POST.get('nome-emergencia2')
    telefone_emergencia2 = request.POST.get('telefone-emergencia2')
    grau_parentesco2 = request.POST.get('grau-parentesco2')
    # Dependentes
    nome_dependente1 = request.POST.get('nome-dependente')
    cpf_dependente1 = request.POST.get('cpf-dependente')
    nascimento_dependente1 = request.POST.get('nascimento-dependente')
    grau_parentesco_dependente1 = request.POST.get('grau-parentesco-dependente')
    nome_dependente2 = request.POST.get('nome-dependente2')
    cpf_dependente2 = request.POST.get('cpf-dependente2')
    nascimento_dependente2 = request.POST.get('nascimento-dependente2')
    grau_parentesco_dependente2 = request.POST.get('grau-parentesco-dependente2')
    nome_dependente3 = request.POST.get('nome-dependente3')
    cpf_dependente3 = request.POST.get('cpf-dependente3')
    nascimento_dependente3 = request.POST.get('nascimento-dependente3')
    grau_parentesco_dependente3 = request.POST.get('grau-parentesco-dependente3')
    nome_dependente4 = request.POST.get('nome-dependente4')
    cpf_dependente4 = request.POST.get('cpf-dependente4')
    nascimento_dependente4 = request.POST.get('nascimento-dependente4')
    grau_parentesco_dependente4 = request.POST.get('grau-parentesco-dependente4')
    try:
        user = Funcionario.objects.get(id_login=id_login)
        user.id_login = id_login
        user.nome = nome
        user.email = email
        user.cor = cor
        user.possui_filhos = possui_filhos
        user.genero = genero
        user.cpf = cpf
        user.estado_civil = estado_civil
        user.grau_escolaridade = grau_escolaridade
        user.cep = cep
        user.rua = rua
        user.numero = numero
        user.bairro = bairro
        user.estado = estado
        user.cidade = cidade
        # Trabalho
        user.empresa = empresa
        user.email_corporativo = email_corporativo
        user.modelo_trabalho = modelo_trabalho
        user.gerente = gerente
        user.departamento = departamento
        user.cargo = cargo
        # Saude
        user.alergia = alergia
        user.tratamento_saude = tratamento_saude
        user.medicamento_continuo = medicamento_continuo
        # Contato
        user.telefonepessoal1 = telefonepessoal1
        user.telefonepessoal2 = telefonepessoal2
        user.nome_emergencia1 = nome_emergencia1
        user.telefone_emergencia1 = telefone_emergencia1
        user.grau_parentesco1 = grau_parentesco1
        user.nome_emergencia2 = nome_emergencia2
        user.telefone_emergencia2 = telefone_emergencia2
        user.grau_parentesco2 = grau_parentesco2
        # Dependentes
        user.nome_dependente1 = nome_dependente1
        user.cpf_dependente1 = cpf_dependente1
        user.nascimento_dependente1 = nascimento_dependente1
        user.grau_parentesco_dependente1 = grau_parentesco_dependente1
        user.nome_dependente2 = nome_dependente2
        user.cpf_dependente2 = cpf_dependente2
        user.nascimento_dependente2 = nascimento_dependente2
        user.grau_parentesco_dependente2 = grau_parentesco_dependente2
        user.nome_dependente3 = nome_dependente3
        user.cpf_dependente3 = cpf_dependente3
        user.nascimento_dependente3 = nascimento_dependente3
        user.grau_parentesco_dependente3 = grau_parentesco_dependente3
        user.nome_dependente4 = nome_dependente4
        user.cpf_dependente4 = cpf_dependente4
        user.nascimento_dependente4 = nascimento_dependente4
        user.grau_parentesco_dependente4 = grau_parentesco_dependente4
        user.save()
    except:
        user = Funcionario()
        user.id_login = id_login
        user.nome = nome
        user.email = email
        user.cor = cor
        user.cpf = cpf
        user.estado_civil = estado_civil
        user.grau_escolaridade = grau_escolaridade
        user.cep = cep
        user.rua = rua
        user.numero = numero
        user.bairro = bairro
        user.estado = estado
        user.cidade = cidade
        # Trabalho
        user.empresa = empresa
        user.email_corporativo = email_corporativo
        user.gerente = gerente
        user.departamento = departamento
        user.cargo = cargo
        # Saude
        user.alergia = alergia
        user.tratamento_saude = tratamento_saude
        user.medicamento_continuo = medicamento_continuo
        # Contato
        user.telefonepessoal1 = telefonepessoal1
        user.telefonepessoal2 = telefonepessoal2
        user.nome_emergencia1 = nome_emergencia1
        user.telefone_emergencia1 = telefone_emergencia1
        user.grau_parentesco1 = grau_parentesco1
        user.nome_emergencia2 = nome_emergencia2
        user.telefone_emergencia2 = telefone_emergencia2
        user.grau_parentesco2 = grau_parentesco2
        # Dependentes
        user.nome_dependente1 = nome_dependente1
        user.cpf_dependente1 = cpf_dependente1
        user.nascimento_dependente1 = nascimento_dependente1
        user.grau_parentesco_dependente1 = grau_parentesco_dependente1
        user.nome_dependente2 = nome_dependente2
        user.cpf_dependente2 = cpf_dependente2
        user.nascimento_dependente2 = nascimento_dependente2
        user.grau_parentesco_dependente2 = grau_parentesco_dependente2
        user.nome_dependente3 = nome_dependente3
        user.cpf_dependente3 = cpf_dependente3
        user.nascimento_dependente3 = nascimento_dependente3
        user.grau_parentesco_dependente3 = grau_parentesco_dependente3
        user.nome_dependente4 = nome_dependente4
        user.cpf_dependente4 = cpf_dependente4
        user.nascimento_dependente4 = nascimento_dependente4
        user.grau_parentesco_dependente4 = grau_parentesco_dependente4
        user.save()
    return redirect(home)
