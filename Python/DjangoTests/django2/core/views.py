from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages # faz com que as mensagens sejam adicionadas no contexto da página
                                    # faz com que as mensagens sejam apresentadas em {% bootstrap_messages %}

from .models import Produto # Para apresentar os dados dos produtos na Index
from django.shortcuts import redirect
# usado pra fazer o reidirecionamento para outra página


def index(request):
    conxtext = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', conxtext)


def contato(request):
    form = ContatoForm(request.POST or None)
    # essa página funciona tanto como get, ou seja, quando simplesmente carrega a página
    # ou como post, quando de fato o usuário preenche dados e submete esses dados

    if str(request.method) == 'POST': # se isso for verdadeiro significa que o usuário enviou dados
        if form.is_valid():         # retorna true se o formulário não tem erros, ou seja, está todo preenchido
            form.send_mail()
            """
            nome = form.cleaned_data['Name'] # 'Name' -> vem da variável Name em forms na classe ContatoForm
            email = form.cleaned_data['email'] # pega-se os dados do formulário com a função form.cleaned_data['']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print(f'Nome: {nome}.') 
            Após recuperar os dados pelo forms.py, não é mais necessário recuperá-los na view
            """

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm() # já que o formulário foi preenchido, deve-se limpá-lo para ser utilizado outra vez
        else:
            messages.error(request, 'Erro ao enviar e-mail :(.')

    context = {
        'form': form
    }# tudo que se quer enviar no contexto do template, coloca-se no dicionário context
    return render(request, 'contato.html', context)


def produto(request):
    print(str(request.user))
    if str(request.user) != 'AnonymousUser':  # permitindo acesso somento para usuário logado no admin
        if str(request.method) == 'POST':
            #lembrando que um formulário para submeter dados é do tipo POST
            form = ProdutoModelForm(request.POST, request.FILES)
            # recuperando dados e arquivos
            # request.POST = upload dos dados
            # request.FILES = upload do arquivo imagem
            if form.is_valid():
                """
                prod = form.save(commit=False)
    
                print(f'Nome: {prod.nome}')
                print(f'Preco: {prod.preco}')
                print(f'Estoque: {prod.estoque}')
                print(f'Imagem: {prod.imagem}')
                
                utilizado para teste, após a criação do MEDIA no settings não é mais necessário
                OBS: o diretório produtos foi excluído
                """
                form.save()
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()
            # caso não seja do tipo POST
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')



