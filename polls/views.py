from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy 
from django.contrib import messages  
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from polls.forms import ProdutoForm    
from polls.models import Produto


class IndexListView(ListView): 
        """[index.html]

                Tela inicial, onde mostra a lista de produtos.
        """
        model = Produto
        template_name = 'index.html' 
        

class CreateView(CreateView):
        """[create.html]

                Tela de cadastro de produtos, contem o formulario.
        """
        model = Produto
        form_class = ProdutoForm
        template_name = 'create.html'
        success_url = reverse_lazy('index')
        success_message = 'Produto Cadastrado com sucesso' 