"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).strip()
quant = frase.count('A')
prim = frase.find("A")+1
ultm = frase.rfind("A")+1
print('Tem exatamente \033[33m{}\033[m letras "A".\n'
      'Aparece a primeira vez na posição \033[31m{}\033[m.\n'
      'Aparece por ultimo na posição \033[31m{}\033[m.'.format(quant, prim, ultm))
