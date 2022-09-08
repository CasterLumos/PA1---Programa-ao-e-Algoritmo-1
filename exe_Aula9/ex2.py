def Media(file):
    soma = 0
    with open(file, 'r') as arquivo:
        for linha in arquivo:
            soma += float(linha.split()[1])

    with open(file, 'r') as arquivo:
        n_linhas = len(arquivo.readlines())
        
    media = soma/n_linhas

    return media

#print(Media('exe_Aula9/notas.txt'))