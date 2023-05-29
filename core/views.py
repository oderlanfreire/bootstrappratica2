from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import ProdutoModel
from django.shortcuts import redirect


def Index(request):
    context = {
        'produtos': ProdutoModel.objects.all()
    }
    return render(request, 'index.html', context)


def Contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.SendEmail()
            messages.sucess(request, 'Email enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o email!')
        
    context = {
        'form':form
    }
    return render(request, 'contato.html', context)


def Produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()      
                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto!')
        else:
            form = ProdutoModelForm()
        context = {
            'form':form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')