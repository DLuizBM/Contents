# Generated by Django 2.2.9 on 2020-06-03 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200603_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='core.Employees'),
        ),
    ]