#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta área de 2m²
l = float(input('Digite a \033[1;31mlargura\033[m: '))
a = float(input('Digite a \033[1;31maltura\033[m: '))
t = 2
print('A area é de \033[33m{0:.3f}m²\033[m.\nSerá necessário \033[33m{1:.3f}ml\033[m de tinta.'.format(l*a,(l*a)/t))
