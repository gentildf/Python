"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
from time import sleep
for c in range(0, 50, 2):
    print(c+2, end=' ')
    sleep(0.5)
