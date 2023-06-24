"""
3. Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
de retorno será 1 se positivo, -1 se negativo e O se for igual a 0.

"""

def verificar_num(num):
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)

verificar_num(-280)