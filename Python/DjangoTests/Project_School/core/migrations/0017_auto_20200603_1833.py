# Generated by Django 2.2.9 on 2020-06-03 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200603_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL, verbose_name='Name'),
        ),
    ]
