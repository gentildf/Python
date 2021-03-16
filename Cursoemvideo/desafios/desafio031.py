'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, obrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''
dist = float(input('\033[1;33mInforme a distância da viagem desejada:\033[m '))
if dist <= 200:
    print(('O valor da sua viagem será de: \033[32mR${:.2f}\033[m'.format(dist*0.5)))
else:
    print('O valor da sua viagem será de: \033[32mR${}\033[m'.format(dist*0.45))
