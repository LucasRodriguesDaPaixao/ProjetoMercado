# Generated by Django 3.0.7 on 2020-07-20 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0007_categoria_fornecedor_funcionario_setor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='FK_cliente',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='compra_produto',
        ),
        migrations.DeleteModel(
            name='Fornecedor',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.DeleteModel(
            name='Setor',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
