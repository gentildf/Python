"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite seu nome completo: ')).strip()
up = nome.upper()
lo = nome.lower()
first = nome.split()
print('O seu nome completo em \033[1;33mmaiúscula\033[m fica: {}'.format(up))
print('O seu nome completo em \033[1;33mminúscula\033[m fica: {}'.format(lo))
print('O seu nome completo tem {} \033[1;33mletras\033[m.'.format(len(''.join(first))))
print('O seu nome tem {} \033[1;33mletras\033[m.'.format(len(first[0])))



