'''
Cire um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
'''
num = int(input('Digite um número para verificar se é par ou ímpar: '))
if num % 2 == 0:
    print('O número informado é \033[1;31mPAR\033[m!')
else:
    print('O número informado é \033[1;31mÍMPAR\033[m!')
