from django import forms


class CriarPostagemForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    content = forms.CharField(required=True, label="Conteudo", widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
