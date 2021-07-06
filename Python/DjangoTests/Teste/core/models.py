from django.db import models


class Admin(models.Model):
    nome = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='#')

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        return self.nome


class Person(models.Model):
    name = models.OneToOneField(Admin, on_delete=models.CASCADE, max_length=15, related_name='person')
    age = models.CharField(max_length=3, default='AGE')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'

    def __str__(self):
        return str(self.name)


class Evaluation(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='evaluation')
    comment = models.TextField(max_length=200, default='#')
    grade = models.DecimalField(max_digits=5, null=True, decimal_places=2)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'

    def __str__(self):
        return self.name
