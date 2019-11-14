from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
)

app_name = 'todos'
urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('novo/', TodoCreateView.as_view(), name='todo_new'),
    path('<int:pk>/deletar', TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/editar', TodoUpdateView.as_view(), name='todo_update'),
]