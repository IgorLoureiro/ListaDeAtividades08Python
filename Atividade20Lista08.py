"""
20. Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial, n!.
"""

def calcular_fatorial(num):
    resultado = num
    while num != 1:
        resultado = resultado * (num - 1)
        num = num - 1
    print(resultado)

calcular_fatorial(8)