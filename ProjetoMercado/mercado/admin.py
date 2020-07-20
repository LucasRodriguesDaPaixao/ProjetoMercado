from django.contrib import admin
from .models import Produto, Compra, Cliente, Fornecedor, Categoria, Setor, Funcionario

# Register your models here.
admin.site.register(Produto)
admin.site.register(Compra)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(Setor)
admin.site.register(Funcionario)