"""
URL configuration for cadastro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_att_cadastro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page),
    path('logar', views.logar, name='logar'),
    path('home', views.home, name='home'),
    path('deslogar', views.deslogar, name='deslogar'),
    path('<str:uf>', views.pegar_cidade, name='pegar_cidades'),
    path('buscacep/<int:cep>', views.busca_cep, name='busca_cep')
]