"""
Faça uma função que receba um número inteiro positivo N e retorne o
superfatorial desse número. O superfatorial de um número N é definida pelo produto dos
N primeiros fatoriais de N. Assim, o superfatorial de 4 é sf(4) = 11*21*31* 4! = 288.
"""
import numpy


def calcular_superfatorial(n):
    Lista = []
    for x in range(n, 1, -1):
        resultado = x
        while x != 1:
            resultado = resultado * (x - 1)
            x = x - 1
        Lista.append(resultado)
    print(f"O super fatorial de {n} é {numpy.prod(Lista)}")



calcular_superfatorial(4)