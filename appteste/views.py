from django.shortcuts import render


def index(request):
    return render(request, "appteste/index.html")


def teste(request, id):
    return render(request, "appteste/teste.html", {"id": id})