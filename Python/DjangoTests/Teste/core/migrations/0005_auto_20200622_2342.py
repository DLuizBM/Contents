# Generated by Django 2.2.9 on 2020-06-22 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200622_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.OneToOneField(max_length=15, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='core.Admin'),
        ),
    ]