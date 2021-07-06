from django import forms
from django.core.mail.message import EmailMessage
# pacote importado para enviar de email
from .models import Produto

# Esse tipo de form, utilizamos para contatos. Existem outras formas de fazer formulários
class ContatoForm(forms.Form): # forms.Form -> o módulo forms tem uma classe chamada Form
    Name = forms.CharField(label='Nome')
    email = forms.CharField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())   # widget faz que seja possível pegar várias linhas

    def send_mail(self): # recuperando os dados digitados pelo usuário, assim como na view
        nome = self.cleaned_data['Name']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:{nome}\nEmail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}\n'

        mail = EmailMessage( #instanciando um objeto da classe que foi feita o import
            subject='Email enviado pelo sistema Django2',
            body=conteudo,
            from_email='noreply@seudominio.com',
            to=['d-luiz@hotmail.com'], #cria uma lista de emails para qual o email resposta deve ser enviado
            headers={'Reply-to': email},
        )
        mail.send()
        # envia o objeto para onde ele for chamado

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']