from django.db import models

class Tarefa(models.Model):
    nome_tarefa = models.CharField(max_length=100, unique=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    data_limite = models.DateField()
    ordem_apresentacao = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.nome_tarefa

class Meta:
    db_table = 'tarefas'
    
        