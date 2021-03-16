#Desafio 003 "Crie um programa que leia dois npumeros e mostre a soma entre eles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('\033[mA soma entre \033[31m{1}\033[m e \033[31m{0}\033[m é igual a \033[31m{2}\033[m'.format(n1, n2, s))
