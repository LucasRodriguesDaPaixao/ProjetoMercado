from django.db import models

# Create your models here.
class Produto(models.Model):
    ID_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100, verbose_name="Nome:")
    data_validade = models.DateField(verbose_name="Data de validade:")
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço:")
    quantidade_produto = models.IntegerField(verbose_name="Quantidade de produtos:")


    def __str__(self):
        return self.nome_produto


class Compra(models.Model):
    ID_compra = models.AutoField(primary_key=True)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço:")
    

class Cliente(models.Model):
    ID_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome:")
    cpf = models.CharField(max_length=15, verbose_name="CPF:")