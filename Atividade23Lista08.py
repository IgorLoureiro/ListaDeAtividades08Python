"""
23. Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a saída para n = 4 seria:
"""

def fazer_triangulo(n):
    i = '*'
    n = n*2-1
    for x in range(1, round(n/2)):
        print(i * x)
    for x in range(round(n/2), 0, -1):
        print(i*x)

fazer_triangulo(30)