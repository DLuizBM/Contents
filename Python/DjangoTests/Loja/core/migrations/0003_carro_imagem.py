# Generated by Django 2.2.9 on 2020-04-15 13:37

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carro'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='imagem',
            field=stdimage.models.StdImageField(default='#', upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]