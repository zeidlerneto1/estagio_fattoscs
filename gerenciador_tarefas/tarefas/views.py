from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .models import Tarefa
from .services import lista_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa

def listar_tarefas_view(request):
    """
    Exibe a lista de tarefas no template.
    """
    
    tarefas = lista_tarefas()
    return render(request, 'tarefas/tarefas.html', {'tarefas': tarefas})

def salvar_ordem_tarefas_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ordem_ids = data.get('ordem', [])  

            Tarefa.objects.all().update(ordem_apresentacao=None)

            for posicao, tarefa_id in enumerate(ordem_ids, start=1):
                tarefa = Tarefa.objects.get(id=tarefa_id)
                tarefa.ordem_apresentacao = posicao  # Atribui a nova ordem
                tarefa.save()

            return JsonResponse({'status': 'success', 'message': 'Ordem salva com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'}, status=405)


def criar_tarefa_view(request):
    """
    Cria uma nova tarefa.
    """
    if request.method == "POST":
        nome_tarefa = request.POST.get('nome_tarefa')
        custo = request.POST.get('custo')
        data_limite = request.POST.get('data_limite')
        ultima_ordem = Tarefa.objects.order_by('ordem_apresentacao').last()
        ordem_apresentacao = ultima_ordem.ordem_apresentacao + 1 if ultima_ordem else 1
        criar_tarefa(nome_tarefa, custo, data_limite, ordem_apresentacao)
        return redirect('listar_tarefas')  
    return render(request, 'tarefas/criar.html')

def editar_tarefa_view(request, tarefa_id):
    """
    Edita uma tarefa existente.
    """
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == "POST":
        nome_tarefa = request.POST.get('nome_tarefa')
        custo = request.POST.get('custo')
        data_limite = request.POST.get('data_limite')

        editar_tarefa(tarefa_id, nome_tarefa, custo, data_limite)

        return redirect('listar_tarefas')

    return render(request, 'tarefas/editar.html', {'tarefa': tarefa})

def excluir_tarefa_view(request, tarefa_id):
    """
    Exclui uma tarefa.
    """
    if request.method == "POST":
        excluir_tarefa(tarefa_id)
        return redirect('listar_tarefas')
    
    tarefa = Tarefa.objects.get(id=tarefa_id)  
    return render(request, 'tarefas/deletar.html', {'tarefa': tarefa})