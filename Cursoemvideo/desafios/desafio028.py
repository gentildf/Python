'''
Escreva um programa que faça o computador "pensar" e um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo cpmputador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
print('\033[33mO computador está pensando em um número entre 1 a 5...\033[m ')
chute = int(input('\033[31mTente adivinhar o número:\033[m '))
pc = randint(1,5)
print('\033[4;33mPROCESSANDO...\033[m')
sleep(2)
print('\033[4mO computador estava pensando no número:\033[32m{}\033[m'.format(pc))
if chute == pc:
    print("\033[1;32mVocê acertou miserávi!!!")
else:
    print('\033[31mChutou errado e acertou a canela do teu brother')
