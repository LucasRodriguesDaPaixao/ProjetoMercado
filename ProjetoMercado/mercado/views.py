from django.shortcuts import render
from .models import Produto, Compra, Cliente, Fornecedor, Categoria, Setor, Funcionario


# Create your views here.
def produto(request):
    return render(request, "mercado/index.html")


def Listagem(request):
    data = {}
    data["Produtos"] = Produto.objects.all()
    return render(request, "mercado/Listagem.html", data)