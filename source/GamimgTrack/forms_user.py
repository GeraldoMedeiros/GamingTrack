from django import forms


class RegisterUserForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'nome',
            'placeholder':'Insira seu nome completo',
        }
    ))
    email = forms.CharField(label="E-mail", max_length=255, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'id':'nome',
            'placeholder':'Insira seu e-mail',
        }
    ))
    login = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'login',
            'placeholder':'Escolha um nome de usuário',
        }
    ))
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'id':'password',
            'placeholder':'Insira uma senha forte',
        }
    ))
    password1 = forms.CharField(max_length=255, label="confirme a senha", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'id':'password',
            'placeholder':'Repita a senha',
        }
    ))
    check = forms.BooleanField(label="Você está de acordo com os nossos termos?", widget=forms.CheckboxInput(
        attrs={
            'class':'form-check-input',
            'id':'check',
        }
    ))


class LoginUserForm(forms.Form):
    login = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'id':'login',
            'placeholder':'Insira seu nome de usuário',
        }
    ))
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'id':'senha',
            'placeholder':'Insira sua senha',
        }
    ))


class ChangeUserPasswordForm(forms.Form):
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=255, label="confirme a nova senha", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, label="senha antiga", widget=forms.PasswordInput)


class ChangeUserEmailForm(forms.Form):
    email = forms.CharField(max_length=255, label="email atual")
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)


class ChangeUserNameForm(forms.Form):
    nome = forms.CharField(max_length=255, label="nickname")
    password = forms.CharField(max_length=255, label="senha", widget=forms.PasswordInput)
