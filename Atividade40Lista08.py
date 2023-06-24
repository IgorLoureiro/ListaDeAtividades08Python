"""
Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele
possui.
"""

def valorespares(x):
    i = 0
    Lista = []
    for z in x:
        if z % 2 == 0:
            i = i + 1
            Lista.append(z)
    print(f"Existem {i} valores pares no Vetor, sendo eles {Lista}")


Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valorespares(Lista)