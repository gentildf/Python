"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

(progressão aritmética = PA)
"""
termo = int(input('Escreva o termo: '))
razao = int(input('Escreva a razão: '))
print(termo, end='')
pa = termo + razao
for c in range(1, 10):
    print(' >', pa, end='')
    pa += razao
