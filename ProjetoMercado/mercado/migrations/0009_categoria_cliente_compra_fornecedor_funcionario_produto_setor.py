# Generated by Django 3.0.7 on 2020-07-20 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mercado', '0008_auto_20200720_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('ID_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=45, verbose_name='Nome Categoria:')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ID_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=100, verbose_name='Nome:')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF:')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('ID_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('nome_fornecedor', models.CharField(max_length=100, verbose_name='Nome:')),
                ('email_fornecedor', models.CharField(max_length=100, verbose_name='Email:')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ:')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone:')),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('ID_setor', models.AutoField(primary_key=True, serialize=False)),
                ('nome_setor', models.CharField(max_length=45, verbose_name='Setor:')),
                ('FK_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('ID_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=100, verbose_name='Nome:')),
                ('data_validade', models.DateField(verbose_name='Data de validade:')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço:')),
                ('quantidade_produto', models.IntegerField(verbose_name='Quantidade de produtos:')),
                ('FK_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Categoria')),
                ('FK_fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('ID_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.CharField(max_length=45, verbose_name='Nome:')),
                ('rg', models.CharField(max_length=15, verbose_name='RG:')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF:')),
                ('FK_setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Setor')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('ID_compra', models.AutoField(primary_key=True, serialize=False)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor total:')),
                ('FK_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercado.Cliente')),
                ('compra_produto', models.ManyToManyField(to='mercado.Produto')),
            ],
        ),
    ]
