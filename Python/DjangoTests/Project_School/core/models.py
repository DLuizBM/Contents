from django.db import models
from django.contrib.auth.models import User


class Admins(models.Model):
    name = models.ForeignKey(User, verbose_name='Name', on_delete=models.CASCADE, related_name='admins')
    bio = models.TextField('Bio', max_length=200, default='')

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return self.name.username


class Employees(models.Model):
    name = models.ForeignKey(User, verbose_name='Name', max_length=20, on_delete=models.CASCADE, related_name='employees')
    birthday = models.CharField(verbose_name='Birthday', max_length=10, help_text='01/01/2020')
    id_number = models.CharField(verbose_name='Id Number', max_length=7, help_text='3141199')

    class Meta:
        verbose_name = 'Employees'
        verbose_name_plural = 'Employeess'

    def __str__(self):
        return self.name.username


class Address(models.Model):
    user = models.OneToOneField(Employees, on_delete=models.CASCADE, related_name="address", default=1)
    country = models.CharField(verbose_name='Country', max_length=10)
    state = models.CharField(max_length=12, default='DF')


class Document(models.Model):
    user = models.OneToOneField(Employees, on_delete=models.CASCADE, related_name="document", default=1)
    type = models.CharField(verbose_name='CPF or ID', max_length=3, default='#')
    number = models.CharField(verbose_name='Number of the document', max_length=12, default='#')
