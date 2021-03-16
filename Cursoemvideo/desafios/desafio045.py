"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint

print('JOGO DE POKENPÔ')
player = int(input('Escolha uma das opções:\n'
                   '\033[32m0 - PEDRA\033[m\n'
                   '\033[33m1 - TESOURA\033[m\n'
                   '\033[34m2 - PAPEL\033[m\n'
                   'Digite aqui o número referente a sua jogada: '))
lista = ['PEDRA', 'TESOURA', 'PAPEL']
pc = randint(0, 2)
print('O computador escolher: \033[1;35m{}\033[m'.format(lista[pc]))
print('Você escolheu: \033[1;35m{}\033[m'.format(lista[player]))

if player == 0:
    if player == pc:
        print('Deu empate')
    elif pc == 2:
        print('Computador venceu!')
    elif pc == 1:
        print('Você venceu!')
    else:
        print('Operação invalida!')
if player == 1:
    if player == pc:
        print('Deu empate')
    elif pc == 0:
        print('Computador venceu!')
    elif pc == 2:
        print('Você venceu!')
    else:
        print('Operação invalida!')
if player == 2:
    if player == pc:
        print('Deu empate')
    elif pc == 1:
        print('Computador venceu!')
    elif pc == 0:
        print('Você venceu!')
    else:
        print('Operação invalida!')
