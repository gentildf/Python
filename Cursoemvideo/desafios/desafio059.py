"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso.
"""
exit = 0
a = float(input('Digite o 1ª valor: '))
b = float(input('Digite o 2ª valor: '))
while exit != 5:
    exit = int(input('''Essas são as opções para tratar os números {} e {}
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Digite a opção: '''.format(a, b)))
    print('-' * 16)
    if exit == 1:
        print('Você escolheu a opção "SOMA"')
        print('{} + {} = {}'.format(a, b, a + b))
    if exit == 2:
        print('Você escolheu a opção "MULTIPLICAR"')
        print('{} x {} = {}'.format(a, b, a * b))
    if exit == 3:
        print('Você escolheu a opção "MAIOR"')
        if a > b:
            print('O número {} é maior que {}.'.format(a, b))
        elif a == b:
            print('O dois números são iguais.')
        else:
            print('O número {} é maior que {}.'.format(b, a))
    if exit == 4:
        print('Você escolheu a opção "NOVOS NÚMEROS"')
        a = float(input('Digite o 1ª valor: '))
        b = float(input('Digite o 2ª valor: '))
    if exit > 5:
        print('Você digitou uma opção invalida.')
    print('-'*16)
print('Você saiu do programa com êxito.')
