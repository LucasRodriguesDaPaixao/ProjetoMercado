# Generated by Django 3.0.7 on 2020-07-20 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0004_compra_fk_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Compra',
        ),
    ]
