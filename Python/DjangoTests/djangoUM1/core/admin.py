from django.contrib import admin
from .models import Post

"""
tudo relacionado ao admin, ocorre no admim
como a função para mostrar o nome e sobrenome

"""

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle', '_author')
    exclude = ['author', ]

    # Herdando todos os objetos e printando os atributos
    for obj in Post.objects.all():
        print(obj.author)
        print(obj.text)

    # Mostrando nome e sobrenome na área de autor
    # como o mostrado é no admin
    def _author(self, instance):
        return f'{instance.author.get_full_name()}'
    # Instance é o Post de models, pega tudo do Post
    # herda de Post, pois está dentro da PostAdmin(admin.register(Post))
    # se fosse outra classe, instance herdaria de outra classe

    # Mostrando apenas os posts referente ao usuário logado, impedindo de ver as configurações
    # de outros usuários.
    def get_queryset(self, request):
        """
        Ess método get_queryset pertence a classe ModelAdmin, pode haver outras formas para esse método
        dependendo da classe.
        get_queryset nada mais é do que o método que faz a consulta ao banco de dados
        get_queryset precisa fazer um request para ter acesso
        importante manter o nome (get_queryset) para funcionar
        :return:
        """
        qs = super(PostAdmin, self).get_queryset(request)
        # retornando o queryset original, passando o nome da classe em que está fazendo(PostAdmin)
        print(f'Sessão:{request.session}')
        print(f'Método:{request.method}')
        print(f'Usuário:{request.user}')
        """
        requisições Http, request
        https://docs.djangoproject.com/en/1.8/ref/request-response/#django.http.HttpRequest.user
        """
        return qs.filter(author=request.user)
    """
    Mesmo fazendo essa alteração, o usuário logado ainda pode criar posts para outro usuário.
    Sendo assim é necessário fazer uma modificação para impedir que se crie posts para outros
    usuários. Para isso é necessário fazer um exclude = ['author', ], que exclui o campo author
    nas opções de post, e reecrever o método save_model.
    save_model é o objeto que salva o objeto na página de admin.
    
    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        """
        obj: é a model Post, logo o atributo author vai receber o nome do usuário logado
        """
        super().save_model(request, obj, form, change)




