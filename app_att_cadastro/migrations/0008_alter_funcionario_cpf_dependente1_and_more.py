# Generated by Django 4.2.7 on 2023-11-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_att_cadastro', '0007_alter_funcionario_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
