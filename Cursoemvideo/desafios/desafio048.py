"""
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
s = 0
for c in range(0, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print('O número {} é ímpar e multiplo de 3'.format(c))
            s += c
print('A soma de todos esses números é: {}'.format(s))
