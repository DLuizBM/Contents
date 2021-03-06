# Generated by Django 3.0.4 on 2020-03-12 18:08

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200312_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('imagem', stdimage.models.StdImageField(upload_to='equipe', verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
