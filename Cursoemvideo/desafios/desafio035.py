"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo
"""
reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
lista = [reta1, reta2, reta3]
lista.sort()
if lista[1] + lista[0] > lista[-1]:
    print('\033[32mAs três retas podem formar um triângulo.\033[m')
else:
    print('\033[31mAs três retas não podem formar um triângulo.\n'
          'Motivo: \033[33m{}m\033[m + \033[33m{}m\033[m não é maior que \033[33m{}m\033[m'.format(lista[0], lista[1], lista[-1]))
