# Generated by Django 3.0.7 on 2020-07-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0012_auto_20200720_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF:'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='rg',
            field=models.CharField(max_length=12, verbose_name='RG:'),
        ),
    ]
