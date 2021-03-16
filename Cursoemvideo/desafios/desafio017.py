#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa.
import math
opo = float(input('Digite o valor do \033[4mcateto oposto\033[m: '))
adj = float(input('Digite o valor do \033[4mcateto adjacente\033[m: '))
hip = math.hypot(opo, adj) #(opo ** 2 + adj ** 2) ** (1/2) é a formula do calculo.
print('O valor da hipotenusa é de: \033[1;31m{:.2f}'.format(hip))

