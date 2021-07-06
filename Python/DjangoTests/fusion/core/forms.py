from django import forms
from django.core.mail.message import EmailMessage


# forms.ModelForm é utilizado quando se faz cadastros, o cadastro nesse projeto é feito no admin
class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):    # função necessário para recuperar os dados
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='d-luiz@hotmail.com',
            to=['d-luiz@hotmail.com', ],
            headers={'Reply-to': email}
        )
        mail.send()