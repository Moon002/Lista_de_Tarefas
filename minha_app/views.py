from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa  # Certifique-se de que a importação do modelo está correta
from .forms import TarefaForm  # Certifique-se de que a importação do formulário está correta

def lista_tarefas(request):
    if request.method == 'POST':
        tarefa_id = request.POST.get('concluir_tarefa')
        if tarefa_id:
            tarefa = Tarefa.objects.get(pk=tarefa_id)
            tarefa.concluida = True
            tarefa.save()
            return redirect('lista_tarefas')

    tarefas = Tarefa.objects.filter(concluida=False)
    return render(request, 'minha_app/lista_tarefas.html', {'tarefas': tarefas})


def cadastra_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'minha_app/cadastra_tarefa.html', {'form': form})

def edita_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'minha_app/edita_tarefa.html', {'form': form, 'tarefa': tarefa})

def exclui_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()
    return redirect('lista_tarefas')

def relatorio_tarefas(request):
    # Lógica para coletar dados de relatório
    tarefas = Tarefa.objects.filter(concluida=True)

    context = {'tarefas': tarefas}
    return render(request, 'minha_app/relatorio_tarefa.html', context)