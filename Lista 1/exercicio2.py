# Escreva um programa para calcular quanto deve ser pago por um produto de acordo
# com a forma de pagamento selecionada por um cliente. O cliente deve informar ao
# programa o valor original do produto. A forma de pagamento é indicada por meio de
# um código (segunda coluna da tabela abaixo). Após receber as entradas necessárias o
# programa deve informar ao cliente o valor do produto com e sem o desconto. O
# programa deve validar se valor do produto e o código do pagamento são válidos.

# Forma de Pagamento            Código Desconto (%)
# À vista em dinheiro ou pix       1        10
# À vista no cartão de crédito     2        5
# Parcelado                        3        1

valorProduto = float(input('Digite o valor do produto'))
validaValor = valorProduto > 0
if(validaValor):
    formaPagamento = float(input('Selecione o metodo de pagamento\r\n \
    À vista em dinheiro ou pix       1\r\n \
    À vista no cartão de crédito     2 \r\n \
    Parcelado                        3 \r\n \
    Código: \
    '))
    validarFormaPagamento = (formaPagamento > 0 and formaPagamento < 4)
    if(validarFormaPagamento):
        if(formaPagamento == 1):
            # desconto de 10%
            desconto = valorProduto - (valorProduto*0.1)
            print('O valor do produto sem desconto é {} e com desconto é {}'.format(
                valorProduto, desconto))
        elif(formaPagamento == 2):
            # desconto de 5%
            desconto = valorProduto - (valorProduto*0.05)
            print('O valor do produto sem desconto é {} e com desconto é {}'.format(
                valorProduto, desconto))
        else:
            # desconto de 1%
            desconto = valorProduto - (valorProduto*0.01)
            print('O valor do produto sem desconto é {} e com desconto é {}'.format(
                valorProduto, desconto))
    else:
        print("Método inválido")
else:
    print("Valor não pode ser nulo ou negativo")
