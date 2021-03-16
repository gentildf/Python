"""
Faça um programa que jogue par ou ímpar om o computador.
O jogo será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('~' * 12, '\033[;32mJOGO DE PAR OU IMPAR\033[m', '~' * 12)
c = 0
while True:
    pc = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolhar PAR ou IMPAR [P/I]: ')).upper()[0]
    player = int(input('Digite um número: '))
    print(f'O computador escolheu o número {pc}.')
    soma = pc + player
    if soma % 2 == 0:
        print(f'A soma dos números {pc} e {player} é {soma}.')
        print(f'Soma deles é PAR.')
        if escolha == 'P':
            print('\033[1;32mVocê ganhou!\033[m')
            c += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
    else:
        print(f'A soma dos números {pc} e {player} é {soma}.')
        print(f'Soma deles é ÍMPAR.')
        if escolha == 'I':
            print('\033[1;32mVocê ganhou!\033[m')
            c += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
print(f'Você venceu \033[33m{c}\033[m vezes.')
