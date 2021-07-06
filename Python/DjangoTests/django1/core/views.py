from django.shortcuts import render
from django.shortcuts import get_object_or_404
# faz a verificação pra saber se existe uma página, se não aprensentará o erro 404

from .models import Produto
from django.http import HttpResponse # para criar uma resposta http, que é o formato que as páginas de erro do Django funcionam
from django.template import loader

# Create your views here.
# Quem possui views são somente as aplicações, são elas que são programadas para que
# o MTV(mvc em outras linguagens) do django funcione.
# quando se muda no arquivo settings.py o DEBUG para False, o python procura em views
# uma função(view) chamada index, uma view django é uma função.


def index(request): # request - a view recebe requisição feita pelo navegador
    """print(request)
    print(request.method)
    print(f"Headers: {request.headers['User-Agent']}")
    print(f'User: {request.user.email}')
    print(dir(request.user))
    # métodos para saber informações do sistema e do usuário
    # usar o terminal, após python manage.py runserver
    # os métodos estão sendo aplicados na página raiz, logo as informações no terminal
    # só serão mostradas, caso estejamos na página raiz no browser. Caso queiramos informações
    # de outras páginas da aplicação, basta aplicar esses métodos nas outras funções, classes.
    """
    produtos = Produto.objects.all() # fazendo a busca no banco de dados
    context = {
        'aprender': 'É necessário aprender django!!',
        'django': 'Django é o melhor!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)
    # é retornada uma renderização do request com um template(página html)

def contato(request):
    print(request.user.email)
    print(f"Usuário: {request.user}")
    print(f'Tipo de request.user: {type(request.user)}')
    if str(request.user) == 'divinoluiz':
        teste = 'Bem vindo Divino Luiz'
    else:
        teste = 'Você não está logado'
    contatos = {
        'Divino': '6198559-7177',
        'usuario': teste
    }
    return render(request, 'contato.html', contatos)


def produto(request, pk):
    print(f'pk: {pk}')
    # product = Produto.objects.get(id=pk)
    # o método get traz um elemento único(de acordo com o elemento passado), e deve-se buscar pelo id, por isso id=pk
    # pois o id vai pegar cada elemento por vez no banco de dados

    product = get_object_or_404(Produto, id=pk)
    # busca o objeto do tipo produto com o id pk, caso não encontre redirecione para a página 404
    context = {
        'produto': product
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html:charset=utf8', status=404)

# essa view recebe 2 parâmetros, request e exception

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html:charset=utf8', status=500)
