from django.db import models
from django.contrib.auth.models import User


class Compromisso(models.Model):

    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    obs = models.TextField(blank=True)
    AG = 'Agendado'
    RL = 'Realizado'
    CL = 'Cancelado'
    status = models.CharField(max_length=20, choices=[(AG, 'Agendado'), (RL, 'Realizado'), (CL, 'Cancelado')],
                              default='Agendado')
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
