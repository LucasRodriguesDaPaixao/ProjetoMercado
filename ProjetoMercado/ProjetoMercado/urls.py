"""
Definition of urls for ProjetoMercado.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from mercado.views import index
from mercado.views import cadastro_produto, produtos, atualizar_produto, deletar_produto
from mercado.views import clientes, cadastro_cliente, atualizar_cliente, deletar_cliente
from mercado.views import fornecedores, cadastro_fornecedor, atualizar_fornecedor, deletar_fornecedor
from mercado.views import categorias, cadastro_categoria, atualizar_categoria, deletar_categoria
from mercado.views import funcionarios, cadastro_funcionario, atualizar_funcionario, deletar_funcionario
from mercado.views import setores, cadastro_setor, atualizar_setor, deletar_setor
from mercado.views import compras, cadastro_compra, atualizar_compra, deletar_compra


urlpatterns = [
    path('', index, name="url_index"),
    ## Produtos
    path('produtos/', produtos, name="url_produtos"),
    path('cadastro_produto/', cadastro_produto, name="url_cadastro_produto"),
    path('atualizar_produto/<int:pk>', atualizar_produto, name='url_atualizar_produto'),
    path('deletar_produto/<int:pk>', deletar_produto, name='url_deletar_produto'),
    ## Clientes
    path('clientes/', clientes, name="url_clientes"),
    path('cadastro_cliente/', cadastro_cliente, name="url_cadastro_cliente"),
    path('atualizar_cliente/<int:pk>', atualizar_cliente, name='url_atualizar_cliente'),
    path('deletar_cliente/<int:pk>', deletar_cliente, name='url_deletar_cliente'),
    ## Fornecedores
    path('fornecedores/', fornecedores, name="url_fornecedores"),
    path('cadastro_fornecedor/', cadastro_fornecedor, name="url_cadastro_fornecedor"),
    path('atualizar_fornecedor/<int:pk>', atualizar_fornecedor, name='url_atualizar_fornecedor'),
    path('deletar_fornecedor/<int:pk>', deletar_fornecedor, name='url_deletar_fornecedor'),
    ## Categorias
    path('categorias/', categorias, name="url_categorias"),
    path('cadastro_categoria/', cadastro_categoria, name="url_cadastro_categoria"),
    path('atualizar_categoria/<int:pk>', atualizar_categoria, name='url_atualizar_categoria'),
    path('deletar_categoria/<int:pk>', deletar_categoria, name='url_deletar_categoria'),
    ## Funcionarios
    path('funcionarios/', funcionarios, name="url_funcionarios"),
    path('cadastro_funcionario/', cadastro_funcionario, name="url_cadastro_funcionario"),
    path('atualizar_funcionario/<int:pk>', atualizar_funcionario, name='url_atualizar_funcionario'),
    path('deletar_funcionario/<int:pk>', deletar_funcionario, name='url_deletar_funcionario'),
    ## Setor
    path('setores/', setores, name="url_setores"),
    path('cadastro_setor/', cadastro_setor, name="url_cadastro_setor"),
    path('atualizar_setor/<int:pk>', atualizar_setor, name='url_atualizar_setor'),
    path('deletar_setor/<int:pk>', deletar_setor, name='url_deletar_setor'),
    ## Compras
    path('compras/', compras, name="url_compras"),
    path('cadastro_compra/', cadastro_compra, name="url_cadastro_compra"),
    path('atualizar_compra/<int:pk>', atualizar_compra, name='url_atualizar_compra'),
    path('deletar_compra/<int:pk>', deletar_compra, name='url_deletar_compra'),
]