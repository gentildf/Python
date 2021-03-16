""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.
Ex: Fulana de souza melo
primeiro: Fulana
ultimo: melo
"""
nome = str(input('Digite seu nome completo: ')).strip()
p = nome.split()
print('O primeiro nome é \033[1;31m{}\033[m e o ultimo nome é \033[1;31m{}\033[m'.format(p[0], p[-1])) #Outra forma seria usar o p[len(p)-1]

