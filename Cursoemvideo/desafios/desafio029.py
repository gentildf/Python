'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''
vel = float(input('\033[7;30mInsira a velocidade registrada: '))
if vel > 80:
    print('\033[31mVocê será multado!\033[m')
    multa = (vel-80)*7
    print('\033[7;31mO valor de multa a pagar será de \033[33mR${:.2f}\033[m'.format(multa))
else:
    print('\033[32mIgual ou abaixo da velocidade permitida. \nContinue assim!')