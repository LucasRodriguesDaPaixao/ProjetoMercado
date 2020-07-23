from django.forms import ModelForm
from .models import Produto, Compra, Cliente, Fornecedor, Categoria, Setor, Funcionario

class ProdutoForm(ModelForm):
    class Meta():
        model = Produto
        fields = ['nome_produto', 'data_validade', 'preco', 'quantidade_produto', 'FK_categoria', 'FK_fornecedor']


class ClienteForm(ModelForm):
    class Meta():
        model = Cliente
        fields = ['nome_cliente', 'cpf']


class FornecedorForm(ModelForm):
    class Meta():
        model = Fornecedor
        fields = ['nome_fornecedor', 'email_fornecedor', 'telefone', 'cnpj']


class CategoriaForm(ModelForm):
    class Meta():
        model = Categoria
        fields = ['nome_categoria']


class FuncionarioForm(ModelForm):
    class Meta():
        model = Funcionario
        fields = ['nome_funcionario', 'cpf', 'rg', 'FK_setor']


class SetorForm(ModelForm):
    class Meta():
        model = Setor
        fields = ['nome_setor', 'FK_categoria']


class CompraForm(ModelForm):
    class Meta():
        model = Compra
        fields = ['FK_cliente', 'compra_produto', 'valor_total']