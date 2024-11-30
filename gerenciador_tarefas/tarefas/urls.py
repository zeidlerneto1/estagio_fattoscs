from django.urls import path
from .views import listar_tarefas_view, criar_tarefa_view, editar_tarefa_view, excluir_tarefa_view, salvar_ordem_tarefas_view

urlpatterns = [
    path('salvar_ordem/', salvar_ordem_tarefas_view, name='salvar_ordem'),
    path('', listar_tarefas_view, name='listar_tarefas'),
    path('criar/', criar_tarefa_view, name='criar_tarefa'),
    path('editar/<int:tarefa_id>/', editar_tarefa_view, name='editar_tarefa'),
    path('deletar/<int:tarefa_id>/', excluir_tarefa_view, name='deletar_tarefa'),
]
