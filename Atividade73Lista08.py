"""
Foi realizada um pesquisa de algumas características físicas de cinco habitantes de certa
região. De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A —
Azuis ou C — Castanhos), cor dos cabelos (L — Louros, P — Pretos ou C — Castanhos) e
idade.

Faça uma função que leia esses dados em um vetor.

e que determine a média de idade das pessoas com olhos casta-
nhos e cabelos pretos.

e que determine e devolva ao programa principal a maior idade
entre os habitantes.

e que determine e devolva ao programa principal a quantidade de
indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham
olhos azuis e cabelos louros.
"""

def ler_pesquisa(x):
    Lista = []
    i = 0
    while i < 5:
        if x[1][i] == "C" and x[2][i] == "P":
            Lista.append(x[3][i])
            i = i + 1
        else:
            i = i + 1
    print(f"A média de idade dos habitantes com cabelos pretos e olhos castanhos é {sum(Lista)/len(Lista)}")
    print(f"O habitante mais velho possui {max(x[3])}")
    i = 0
    Lista.clear()
    while i < 5:
        if x[0][i] == "feminino" and x[1][i] == "A" and x[2][i] == "L" and 17 < x[3][i] < 36:
            Lista.append(x[3][i])
            i = i + 1
        else:
            i = i + 1
    print(f"A quantidade de individuos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que tenham "
          f"olhos azuis e cabelos louros é de {len(Lista)}")


MatrizPesquisa = [["masculino","feminino","masculino","feminino","masculino"], ["A", "C", "C", "C", "A"],
                  ["L", "P", "C", "L", "C"], [18, 19, 20, 21, 22]]

ler_pesquisa(MatrizPesquisa)