'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
from datetime import date
ano = int(input('Digite o ano a ser analisado: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 400 == 0):
    print('O ano \033[31m{}\033[m é um ano bissexto.'.format(ano))
else:
    print('O ano \033[31m{}\033[m não é um ano bissexto'.format(ano))
