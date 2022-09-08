num = int(input("Digite um número:\r\n"))


with open('tabuada.txt', 'w') as arquivo:
    for i in range(11):
        arquivo.write(str(i*num)+'\r\n')