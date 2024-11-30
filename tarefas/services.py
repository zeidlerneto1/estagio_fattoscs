from .models import Tarefa
from django.core.exceptions import ValidationError

def lista_tarefas():
    return Tarefa.objects.all().order_by('ordem_apresentacao')

def criar_tarefa(nome_tarefa, custo, data_limite, ordem_apresentacao):
    
    if ordem_apresentacao is None:
        ultima_ordem = Tarefa.objects.order_by('ordem_apresentacao').last()
        ordem_apresentacao = ultima_ordem.ordem_apresentacao + 1 if ultima_ordem else 1
    
    tarefa = Tarefa.objects.create(
        nome_tarefa=nome_tarefa,
        custo=custo,
        data_limite=data_limite,
        ordem_apresentacao=ordem_apresentacao
    )
    return tarefa
def editar_tarefa(tarefa_id, nome_tarefa, custo, data_limite):

    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.nome_tarefa = nome_tarefa
    tarefa.custo = custo
    tarefa.data_limite = data_limite
    tarefa.save()
    return tarefa

def excluir_tarefa(tarefa_id):
    
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    
    
    
    

    