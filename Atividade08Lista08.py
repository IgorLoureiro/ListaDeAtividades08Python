"""
8. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = va2 +b2. Faça uma função que receba os valores de a e b e calcule o
valor da hipotenusa através da equação.
"""

def calcular_hipotenusa(a, b):
    num = ((a**2) + (b**2))**(1/2)
    print(f"A hipotenusa dos numeros {a} e {b} é igual a {num}")


calcular_hipotenusa(8, 12)