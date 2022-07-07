flag = True
count = 0
soma = 0
while(flag):
    valor = (input("Digite um número:\r\nR:"))
    if(valor == 'p'):
        flag = False
    else:
        count = count + 1
        soma = soma + int(valor)
print('O media final foi: {}'.format(soma/count))