from django.shortcuts import render, redirect
from .models import Produto, Compra, Cliente, Fornecedor, Categoria, Setor, Funcionario
from .form import ProdutoForm, ClienteForm, FornecedorForm, CategoriaForm, FuncionarioForm, SetorForm, CompraForm

#Create your views here.
def index(request):
    return render(request, "mercado/html/index.html")


## Produtos
def produtos(request):
    data = {}
    data["Produtos"] = Produto.objects.all()
    return render(request, "mercado/html/produtos.html", data)


def cadastro_produto(request):
    data = {}
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_produtos')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_produto.html', data)


def atualizar_produto(request, pk):
    data = {}
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('url_produto')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_produto.html', data)


def deletar_produto(request, pk):
    produto = Produto.objects.get(pk=pk)

    produto.delete()
    return redirect('url_produtos')


## Clientes
def clientes(request):
    data = {}
    data["Clientes"] = Cliente.objects.all()
    return render(request, "mercado/html/clientes.html", data)


def cadastro_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_clientes')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_cliente.html', data)


def atualizar_cliente(request, pk):
    data = {}
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('url_clientes')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_cliente.html', data)


def deletar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)

    cliente.delete()
    return redirect('url_clientes')


## Fornecedores
def fornecedores(request):
    data = {}
    data["Fornecedores"] = Fornecedor.objects.all()
    return render(request, "mercado/html/fornecedores.html", data)


def cadastro_fornecedor(request):
    data = {}
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_fornecedores')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_fornecedor.html', data)


def atualizar_fornecedor(request, pk):
    data = {}
    cliente = Fornecedor.objects.get(pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('url_fornecedores')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_fornecedor.html', data)


def deletar_fornecedor(request, pk):
    cliente = Fornecedor.objects.get(pk=pk)

    cliente.delete()
    return redirect('url_fornecedores')


## Categorias
def categorias(request):
    data = {}
    data["Categorias"] = Categoria.objects.all()
    return render(request, "mercado/html/categorias.html", data)


def cadastro_categoria(request):
    data = {}
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_categorias')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_categoria.html', data)


def atualizar_categoria(request, pk):
    data = {}
    categoria = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('url_categoria')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_categoria.html', data)


def deletar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    categoria.delete()
    return redirect('url_categorias')


## Funcionarios
def funcionarios(request):
    data = {}
    data["Funcionarios"] = Funcionario.objects.all()
    return render(request, "mercado/html/funcionarios.html", data)


def cadastro_funcionario(request):
    data = {}
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_funcionarios')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_funcionario.html', data)


def atualizar_funcionario(request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('url_funcionarios')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_funcionario.html', data)


def deletar_funcionario(request, pk):
    funcionario = Funcionario.objects.get(pk=pk)

    funcionario.delete()
    return redirect('url_funcionarios')


## Setor
def setores(request):
    data = {}
    data["Setores"] = Setor.objects.all()
    return render(request, "mercado/html/setores.html", data)


def cadastro_setor(request):
    data = {}
    form = SetorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_setores')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_setor.html', data)


def atualizar_setor(request, pk):
    data = {}
    setor = Setor.objects.get(pk=pk)
    form = SetorForm(request.POST or None, instance=setor)

    if form.is_valid():
        form.save()
        return redirect('url_setor')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_setor.html', data)


def deletar_setor(request, pk):
    setor = Setor.objects.get(pk=pk)

    setor.delete()
    return redirect('url_setor')


## Compras
def compras(request):
    data = {}
    data["Compras"] = Compra.objects.all()
    return render(request, "mercado/html/compras.html", data)


def cadastro_compra(request):
    data = {}
    form = CompraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_compras')
    
    
    data['form'] = form
    return render(request, 'mercado/html/cadastro_compra.html', data)


def atualizar_compra(request, pk):
    data = {}
    compra = Compra.objects.get(pk=pk)
    form = CompraForm(request.POST or None, instance=compra)

    if form.is_valid():
        form.save()
        return redirect('url_compras')

    data['form'] = form
    return render(request, 'mercado/html/cadastro_compra.html', data)


def deletar_compra(request, pk):
    compra = Compra.objects.get(pk=pk)

    compra.delete()
    return redirect('url_compras')