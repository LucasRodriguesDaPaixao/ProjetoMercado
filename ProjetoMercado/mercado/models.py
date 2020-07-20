from django.db import models

# Create your models here.
class Cliente(models.Model):
    ID_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome:")
    cpf = models.CharField(max_length=15, verbose_name="CPF:")


    def __str__(self):
        return self.nome_cliente


class Fornecedor(models.Model):
    ID_fornecedor = models.AutoField(primary_key=True)
    nome_fornecedor = models.CharField(max_length=100, verbose_name="Nome:")
    email_fornecedor = models.CharField(max_length=100, verbose_name="Email:")
    cnpj= models.CharField(max_length=20, verbose_name="CNPJ:")
    telefone = models.CharField(max_length=11, verbose_name="Telefone:")

    def __str__(self):
        return self.nome_fornecedor


class Categoria(models.Model):
    ID_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=45, verbose_name="Nome Categoria:")


    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    ID_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100, verbose_name="Nome:")
    data_validade = models.DateField(verbose_name="Data de validade:")
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço:")
    quantidade_produto = models.IntegerField(verbose_name="Quantidade de produtos:")
    FK_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    FK_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome_produto
    

class Setor(models.Model):
    ID_setor = models.AutoField(primary_key=True)
    nome_setor = models.CharField(max_length=45, verbose_name="Setor:")
    FK_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome_setor


class Funcionario(models.Model):
    ID_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=45, verbose_name="Nome:")
    rg = models.CharField(max_length=15, verbose_name="RG:")
    cpf = models.CharField(max_length=15, verbose_name="CPF:")
    FK_setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_funcionario


class Compra(models.Model):
    ID_compra = models.AutoField(primary_key=True)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor total:")
    FK_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    compra_produto = models.ManyToManyField(Produto)

    def __str__(self):
        return "Compra: {} ".format(self.ID_compra)
