from django.db import models


class Base(models.Model):
    criacao = models.DateField(auto_now_add=True)
    atualizacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    # link de acesso ao curso, unique=True, cada curso vai ter seu link

    class Meta: # Meta é apenas uma convenção
        # O Django usa esta convenção apenas para evitar conflito de nomes entre
        # as opções de configuração da classe e os atributos (os descritores)
        # que definem os campos do model.
        verbose_name = 'Curso'
        verbose_name_plural = 'CURSOS'
        ordering = ['id']
        # feita a paginação, o ordering ordena por id, se for colocar ['-id']
        # ordena em ordem contrária

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    # blank=True: o comentário não é obrigatório
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'AVALIAÇÕES'
        unique_together = ['email', 'curso']
        # cada pessoa com 'email', só pode avaliar uma vez aquele curso
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso com nota {self.avaliacao}'