"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.

"""
from random import randint

pc = randint(0, 10)
play = 110
count = 0
print('---- \033[1;31mADIVINHE EM QUE NÚMERO O COMPUTADOR ESTÁ PENSANDO\033[m ----')
while play != pc:
    play = int(input('Digite um número de 0 a 10: '))
    count += 1
print('Você acertou! Foram \033[33m{}\033[m tentativas até acertar.'.format(count))
print('O número era \033[32m{}\033[m.'.format(pc))
