"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
lista = [num1, num2, num3]
lista.sort()
print('O número \033[1;33mmenor\033[m é: {}'.format(lista[0]) +
      '\nO número \033[1;33mmaior\033[m é: {}'.format(lista[-1]))
