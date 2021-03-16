#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print(19* '\033[33m-_\033[m')
pa = float(input('Digite o preço atual:\033[32m R$\033[m'))
print(19* '\033[33m-_\033[m')
vd = int(input('Digite o \033[1;33mdesconto\033[m a ser aplicado: '))
pn = pa*(vd/100)
print(19* '\033[33m-_\033[m')
print('O preço com \033[4;33mdesconto\033[m fica: \033[32mR${:.2f}\033[m'.format(pa-pn))
