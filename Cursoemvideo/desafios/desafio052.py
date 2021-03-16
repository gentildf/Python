"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""
n = int(input('Digite um número para verificar se ele é primo ou não: '))
count = 0
for c in range(1, n + 1):
    p = n % c
    print('Fazendo a divisão de {} por {} o resto será de {}.'.format(n, c, p))
    if p == 0:
        count += 1
if count == 2:
    print('Esse número é primo.')
else:
    print('Esse número não é primo.')
