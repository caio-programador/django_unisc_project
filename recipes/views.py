from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse("Olá Mundo! Bem vindo ao contato do site.")


def sobre(request):
    return HttpResponse("Olá Mundo! Bem vindo ao sobre do site.")


def teste(request, id):
    return HttpResponse("Teste: {id}".format(id=id))