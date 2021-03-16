#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira de 6.  Math
"""import math
n = float(input('Digite um número real: '))
print('A porção inteira do número é: {}'.format(math.floor(n)))"""
import math
num = float(input('\033[4mDigite um valor:\033[m '))
print('\033[4mA porção inteira do número\033[4;33m {}\033[4m é \033[4;33m{}\033[4m'.format(num, int(num)))
