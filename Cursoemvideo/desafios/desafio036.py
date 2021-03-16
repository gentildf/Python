"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
"""
print(('\033[35m>\033[m' * 6) + ' \033[1mEMPRÉSTIMOS URGENTES\033[m ' + (6 * '\033[35m<\033[m'))
valor_casa = float(input('\033[1;33mDigite o valor da casa que deseja comprar:\033[m '))
salario_comprador = float(input('\033[1;33mDigite qual sua renda mensal:\033[m '))
parcelas = int(input('\033[1;33mDigite o número de parcelas que deseja pagar:\033[1;33m '))
calc_prest = (valor_casa / parcelas)
porc_renda = (salario_comprador * 30 / 100)
if calc_prest <= porc_renda:
    print('\033[32mO empréstimo foi \033[1;32mACEITO!\n'
          'O imóvel de valor R$\033[33m{:.2f}\033[32m será parcelado em \033[33m{}\033[32m vezes.\n'
          'As parcelas ficaram no valor de R$\033[33m{:.2f}\033[33m.'.format(valor_casa, parcelas, calc_prest))
else:
    print('\033[31mO empréstimo foi \033[1;31mNEGADO\033[31m!\n'
          'As parcelas estão acima do limite disponível para sua solicitação.\n'
          'As parcelas ficaram no valor de \033[33m{:.2f}\033[31m reais.\n'
          'Excedendo 30% que é \033[33m{:.2f}\033[31mdo seu salário reais.'.format(calc_prest, porc_renda))
