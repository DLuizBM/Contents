# Generated by Django 2.2.9 on 2020-06-04 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200603_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='#', max_length=3, verbose_name='CPF or ID')),
                ('number', models.CharField(default='#', max_length=12, verbose_name='Number of the document')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documente', to='core.Employees')),
            ],
        ),
    ]
