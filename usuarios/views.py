from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def cadastro(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else: #Cadastra user
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já existe esse user")
        
        user = User.objects.create_user(username=username, email=email, password=senha, first_name=nome, last_name=sobrenome)
        return HttpResponse("Cadastrado com sucesso meu pêxe")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("Logado e autenticado")
        else:
            return HttpResponse("Email ou senha inválidos")


def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse("Plataforma")
    return HttpResponse("Você precisa estar logado")