"""
Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exem-
plo, a saída para n = 6 seria:
"""

def fazer_triangulo(n):
    i = 0

    for x in range(1, n):
        while i != n:
            print(" ", end="")
            i = i + 1
        i = x
        print('*' * (2*x-1))

fazer_triangulo(6)