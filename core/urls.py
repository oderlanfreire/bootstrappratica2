from django.urls import path
from .views import Index, Contato, Produto

urlpatterns = [
    path('', Index, name='index'),
    path('contato/', Contato, name='contato'),
    path('produto/', Produto, name='produto'),
]
