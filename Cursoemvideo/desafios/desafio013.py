#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sa = float(input('\33[7;30mDigite o salário atual:\033[m '))
porc = sa*(15/100)
print('O salário com aumento de \033[33m15%\033[m ficou em: \033[32m{:.2f}\033[m'.format(sa+porc))
