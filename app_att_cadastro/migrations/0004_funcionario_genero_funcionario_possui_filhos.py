# Generated by Django 4.2.7 on 2023-11-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_att_cadastro', '0003_remove_funcionario_usuario_funcionario_id_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='genero',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='possui_filhos',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
