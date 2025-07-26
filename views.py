from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao

@login_required
def calculadora_view(request):
    resultado = None
    historico = Operacao.objects.filter(usuario=request.user).order_by('-criado_em')[:5]

    if request.method == "POST":
        a = float(request.POST['operando1'])
        b = float(request.POST['operando2'])
        operador = request.POST['operador']

        if operador == '+':
            resultado = a + b
        elif operador == '-':
            resultado = a - b
        elif operador == '*':
            resultado = a * b
        elif operador == '/':
            resultado = a / b if b != 0 else "Erro"

        if isinstance(resultado, float):
            Operacao.objects.create(
                usuario=request.user,
                operando1=a,
                operando2=b,
                operador=operador,
                resultado=resultado
            )

    return render(request, 'core/calculadora.html', {
        'resultado': resultado,
        'historico': historico
    })
