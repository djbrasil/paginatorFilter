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
        model = Produto
        template_name = 'index.html' 
        paginate_by = 5
        
        def get_queryset(self):
                query = self.request.GET.get('nome')
                print(query)
                if query:
                        q = self.model.objects.filter(nome__icontains=query)
                else:
                        q = self.model.objects.all()
                return q

class CreateView(CreateView): 
        model = Produto
        form_class = ProdutoForm
        template_name = 'form.html'
        success_url = reverse_lazy('index')
        success_message = 'Produto Cadastrado com sucesso' 
        

class UpdateView(UpdateView): 
        model = Produto
        form_class = ProdutoForm
        template_name = 'form.html'
        success_url = reverse_lazy('index')
        success_message = 'Produto Cadastrado com sucesso'
        
        
class DeleteView(DeleteView): 
        model = Produto 
        template_name = 'delete.html'
        success_url = reverse_lazy('index')
        success_message = 'Produto Deletado com sucesso' 
        