flag = True
maiorValor = 0;
while(flag):
    valor = int(input("Digite um número:\r\nR:"))
    if(valor > maiorValor):
        maiorValor = valor
    if(valor == -1):
        flag = False
print('O maior valor digitado foi: {}'.format(maiorValor))