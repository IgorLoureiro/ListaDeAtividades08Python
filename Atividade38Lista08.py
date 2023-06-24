"""
Faça uma função que receba um número inteiro positivo n e retorne o fa-
torial exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado
à potência de n — 1, que por sua vez é elevado à potência de n — 2 e assim em diante.
"""

def calcular_fatorialexponencial(n):
    Lista = []
    i = 0
    resultado = 0
    for x in range(1, n+1):
        Lista.append(x)
    for z in range(len(Lista)-1, 1, -1):
        if i == 0:
            resultado = (Lista[z])**(Lista[z-1])
            i = i + 1
        else:
            resultado = resultado**(Lista[z])
    print(f"O fatorial exponencial de {n} é igual a {resultado}")

calcular_fatorialexponencial(4)
