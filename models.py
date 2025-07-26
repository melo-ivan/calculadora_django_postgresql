from django.db import models
from django.contrib.auth.models import User

class Operacao(models.Model):
    OPERACOES = [
        ('+', 'Soma'),
        ('-', 'Subtração'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    operando1 = models.FloatField()
    operando2 = models.FloatField()
    operador = models.CharField(max_length=1, choices=OPERACOES)
    resultado = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operando1} {self.operador} {self.operando2} = {self.resultado}"
