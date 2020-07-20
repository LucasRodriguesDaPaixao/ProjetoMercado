from django.contrib import admin
from .models import Produto, Compra, Cliente

# Register your models here.
admin.site.register(Produto)
admin.site.register(Compra)
admin.site.register(Cliente)