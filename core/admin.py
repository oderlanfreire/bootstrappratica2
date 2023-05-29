from django.contrib import admin
from .models import ProdutoModel


@admin.register(ProdutoModel)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')


