#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = input('\033[7;30mDigite o primeiro nome:\033[m ')
n2 = input('\033[7;30mDigite o segundo nome:\033[m ')
n3 = input('\033[7;30mDigite o terceiro nome:\033[m ')
n4 = input('\033[7;30mDigite o quarto nome:\033[m ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[31mA ordem de apresentação será:\033[m\n'
      '\033[4m{}'.format(lista))
