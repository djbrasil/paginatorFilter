from django import forms
from polls.models import Produto

# Forms do Revisão Manual
class ProdutoForm(forms.ModelForm):
        class Meta:
                model = Produto
                fields = ['id', 'nome', 'preco','descricao']
