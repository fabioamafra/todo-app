from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView

app_name = 'todos'
urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('novo/', TodoCreateView.as_view(), name='todo_new'),
]