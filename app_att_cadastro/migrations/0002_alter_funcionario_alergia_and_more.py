# Generated by Django 4.2.7 on 2023-11-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_att_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='alergia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf_dependente4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_parentesco2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_parentesco_dependente1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_parentesco_dependente2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_parentesco_dependente3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='grau_parentesco_dependente4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='medicamento_continuo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nascimento_dependente1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nascimento_dependente2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nascimento_dependente3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nascimento_dependente4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome_dependente1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome_dependente2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome_dependente3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome_dependente4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='nome_emergencia2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone_emergencia2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefonepessoal2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tratamento_saude',
            field=models.TextField(blank=True, null=True),
        ),
    ]
