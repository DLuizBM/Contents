# Generated by Django 3.0.2 on 2020-01-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=20, verbose_name='E-mail')),
            ],
        ),
    ]