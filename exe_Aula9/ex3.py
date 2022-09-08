import math
from ex2 import Media

def DesvioPadrao(file):
    soma = 0
    media = Media(file)
    with open(file, 'r') as arquivo:
        for linha in arquivo:
            soma += (float(linha.split()[1])-media)**2

    with open(file, 'r') as arquivo:
        n_linhas = len(arquivo.readlines())

    desvioPadrao = math.sqrt(soma/n_linhas)

    return desvioPadrao


#print(DesvioPadrao('exe_Aula9/notas.txt'))
