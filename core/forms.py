from django import forms
from django.core.mail.message import EmailMessage

from .models import ProdutoModel


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def SendEmail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        
        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body= conteudo,
            from_email= 'contato@yourdomain.com',
            to = ['contato@yourdomain.com',],
            headers={'Reply-To':email},)
        mail.send()
        

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = ['nome', 'preco', 'estoque', 'imagem']