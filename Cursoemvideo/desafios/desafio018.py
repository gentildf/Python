#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos,tan,sin,radians
ang = float(input('\033[4mDigite o ângulo para saber os valores de \033[4;33mseno\033[4m, \033[4;33mcoseno\033[4m e \033[4;33mtangente\033[4m:\033[m '))
co = cos(radians(ang))
se = sin(radians(ang))
ta = tan(radians(ang))
print('O valor do \033[33mcoseno\033[m de {0} é {1:.2f}.\n'
      'O valor do \033[33mcoseno\033[m de {0} é {2:.2f}.\n'
      'O valor da \033[33mtangente\033[m de {0} é {3:.2f}.'
      .format(ang, co, se, ta))