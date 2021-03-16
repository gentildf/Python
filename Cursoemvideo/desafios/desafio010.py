#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input('Digite quanto dinheiro tem na sua carteira: '))
#d = float(input('Digite o valor do dólar atual: '))
do = float(3.27)
print('O valor do dólar é: \033[32m{0}\033[m.\nVocê pode comprar \033[32m{1:.2f}\033[m dólares.'.format(do, n/do))
