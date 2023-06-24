"""
52. Escreva uma função que recebe uma matriz quadrada de ordem 3 e calcule a sua trans-
posta (se B é a matriz transposta de A então aij = bji).
"""

def transposta(x):
    Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    i2 = 0
    o = 2
    o2 = 2
    while i != 3:
        Matriz[o][o2] = x[i][i2]
        o2 = o2 - 1
        i2 = i2 + 1
        if i2 == 3:
            o2 = 2
            i2 = 0
            o = o - 1
            i = i + 1
    print(x)
    print(Matriz)

Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposta(Matriz)