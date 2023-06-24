"""
Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma
dos elementos que estão na diagonal secundária.
"""
import random

def calculardiagonalmatriz(x):
    Lista = []
    Lista.append(x[0][2])
    Lista.append(x[1][1])
    Lista.append(x[2][0])

    print(f"A soma dos valores da diagonal secundária é igual a {sum(Lista)}")

Lista = []
for n in range(1, 4):
    r = random.randint(1, 101)
    Lista.append([r] * 3)

calculardiagonalmatriz(Lista)
