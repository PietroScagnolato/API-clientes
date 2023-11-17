# Generated by Django 4.2.7 on 2023-11-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_cliente_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
