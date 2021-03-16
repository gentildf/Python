"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preco normal.
- 3x ou mais no cartão: 20% de juros.
"""
valor = float(input('\033[1;31mDigite o valor do produto:\033[m '))
forma = int(input('\033[1;33mQual será a forma de pagamento?'
                  '\n\033[1;34m1 - À vista dinheiro/cheque\033[m'
                  '\n\033[1;34m2 - À vista no cartão\033[m'
                  '\n\033[1;34m3 - Em até 2x no cartão\033[m'
                  '\n\033[1;34m4 - 3x ou mais no cartão\033[m\n'
                  '\033[7;30mDigite a opção desejada:\033[m '))
if forma == 1:
    paga = valor - (valor * 10 / 100)
    print('\033[32mVocê escolheu a forma de pagamento " \033[1;33mÀ vista dinheiro/cheque\033[m "')
    print('\033[32mO valor do produto é de R$\033[33m{:.2f}\033[32m. Nessa forma de pagamento será aplicado '
          '\033[33m10\033[32m% de desconto.'.format(valor))
    print('\033[32mO valor com desconto é de R$\033[33m{:.2f}\033[32m'.format(paga))
elif forma == 2:
    paga = valor - (valor * 5 / 100)
    print('\033[32mVocê escolheu a forma de pagamento " \033[33mÀ vista no cartão\033[32m "')
    print('O valor do produto é de R$\033[33m{:.2f}\033[32m. Nessa forma de pagamento será aplicado '
          '\033[33m5\033[32m% de desconto.'.format(valor))
    print('O valor com desconto é de R$\033[33m{:.2f}\033[32m'.format(paga))
elif forma == 3:
    print('\033[32mVocê escolheu a forma de pagamento " \033[33mEm até 2x no cartão\033[32m "')
    print('O valor do produto é de R$\033[33m{:.2f}\033[32m.'.format(valor))
elif forma == 4:
    paga = valor + (valor * 20 / 100)
    print('\033[32mVocê escolheu a forma de pagamento " \033[33m3x ou mais no cartão\033[32m "')
    print('O valor do produto é de R$\033[33m{:.2f}\033[32m. Nessa forma de pagamento é aplica '
          '\033[33m20\033[32m% de juros.'.format(valor))
    print('O valor atualizado é de R$\033[33m{:.2f}\033[32m'.format(paga))
else:
    print('Você digitou uma opção \033[1;31mINVALIDA\033[m. Refaça a operação.')
