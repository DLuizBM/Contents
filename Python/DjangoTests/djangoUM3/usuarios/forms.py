from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario


# Formulário para a criação do usuário
class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'} # altera os nomes dos campos apresentados no momento de inserir os dados

    def save(self, commit=True): # commit, configuração que vem do próprio método save, help(UserCreationForm.save)
        print(f'Self.forms', self)
        print(f'Dir.forms', dir(self))
        user = super().save(commit=False) # recuperando o usuário
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


# Formulário para a alteração do usuário
class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')