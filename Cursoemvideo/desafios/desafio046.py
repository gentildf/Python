"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(1)
    if c == 1:
        print(0)
        print(emoji.emojize(":sparkles: :tada: \033[1;31mFOGOS!\033[m :tada: :sparkles:", use_aliases=True))
