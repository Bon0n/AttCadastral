# Generated by Django 4.2.7 on 2023-11-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_att_cadastro', '0004_funcionario_genero_funcionario_possui_filhos'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='modelo_trabalho',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
