with open('exe_Aula9/notas.txt') as arquivo:
    for linha in arquivo:
        nota = float(linha.split()[1])
        if(nota<5):
            with open('reprovados.txt', 'a')as reprovados:
                reprovados.write(linha)
        elif(nota<6):
            with open('recuperacao.txt', 'a')as recuperados:
                recuperados.write(linha)
        else:
            with open('aprovados.txt', 'a')as aprovados:
                aprovados.write(linha)