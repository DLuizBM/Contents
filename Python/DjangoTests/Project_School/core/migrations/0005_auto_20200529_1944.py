# Generated by Django 2.2.9 on 2020-05-29 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200529_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admins',
            options={'verbose_name': 'Administrator', 'verbose_name_plural': 'Administrators'},
        ),
        migrations.RemoveField(
            model_name='admins',
            name='text',
        ),
        migrations.AddField(
            model_name='admins',
            name='bio',
            field=models.TextField(default='', max_length=200, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='admins',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Name'),
        ),
    ]