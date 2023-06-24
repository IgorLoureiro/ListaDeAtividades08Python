"""
Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna a soma dos
seus elementos.
"""
import random

Matriz = []
for n in range(4):
    Matriz.append([0] * 4)

i = 0
i2 = 0
while i != 4:
    Matriz[i][i2] = random.randint(1, 101)
    i2 = i2 + 1
    if i2 == 4:
        i2 = 0
        i = i + 1

def calcular_valoresMatriz(x):
    print(f"O valor das soma de todos os numeros da matriz é de "
          f"{sum(Matriz[1]) + sum(Matriz[2]) + sum(Matriz[3]) + sum(Matriz[0])}")

print(Matriz)
calcular_valoresMatriz(Matriz)