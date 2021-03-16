#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhio.
from random import choice
from time import sleep
alu1 = input('\033[33mDigite o nome do primeiro aluno: ')
alu2 = input('Digite o nome do segundo aluno: ')
alu3 = input('Digite o nome do terceiro aluno: ')
alu4 = input('Digite o nome do quarto aluno:\033[m ')
alu5 = [alu1, alu2, alu3, alu4]
print('Os alunos a serem sorteados para apagador o quadro são:\n'
      '\033[1m{}\n'
      '{}\n'
      '{}\n'
      '{}\033[m'
      .format(alu1, alu2, alu3, alu4), '\n')
print('SORTEANDO.......')
sleep(5)
print('O aluno sorteado foi: \033[31m{}\033[m'.format(choice(alu5))
      )

