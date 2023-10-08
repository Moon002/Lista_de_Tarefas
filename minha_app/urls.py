from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('cadastra/', views.cadastra_tarefa, name='cadastra_tarefa'),
    path('edita/<int:id>/', views.edita_tarefa, name='edita_tarefa'),
    path('exclui/<int:id>/', views.exclui_tarefa, name='exclui_tarefa'),
]
