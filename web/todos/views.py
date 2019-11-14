from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TodoListView(ListView):
    model = Todo

class TodoDetailView(DetailView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    success_url = reverse_lazy('todos:todo_list')
    fields = ['todo', 'done']

class TodoUpdateView(UpdateView):
    model = Todo
    success_url = reverse_lazy('todos:todo_list')
    fields = ['todo', 'done']

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos:todo_list')
    