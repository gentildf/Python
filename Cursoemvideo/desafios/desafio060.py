"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120

(while not 0) pode ser isso

fazer de duas maneiras. for e while para treinar.
"""
"""
count = int(input('Digite um número: '))
fator = 1
i = 2
conta = count
print('{}! = {}'.format(count, count), end='')
while count >= i:
    conta = conta - 1
    print('x{}'.format(conta), end='')
    fator = fator * i
    i = i + 1
print(' = {}'.format(fator))
"""
count = int(input('Digite um número: '))
fator = 1
i = 2
conta = count
print('{}! = {}'.format(count, count), end='')
for c in range(1, count):
    conta = conta - 1
    print('x{}'.format(conta), end='')
    fator = fator * i
    i = i + 1
print(' = {}'.format(fator))
