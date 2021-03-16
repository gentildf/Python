"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
v_saq = int(input('Você deseja sacar quanto? R$ '))
saque = v_saq
cont_cinq = cont_vint = cont_dez = cont_um = 0
while saque >= 50:
    cont_cinq += 1
    saque -= 50
while saque >= 20:
    cont_vint += 1
    saque -= 20
while saque >= 10:
    cont_dez += 1
    saque -= 10
while saque >= 1:
    cont_um += 1
    saque -= 1
print(f'Você solicitou o saque no valor de R${v_saq}'
      f'\nSerão entregue a seguinte quantidade de cédulas:')
if cont_cinq > 0:
    print(f'Cédulas de R$50: {cont_cinq}')
if cont_vint > 0:
    print(f'Cédulas de R$20: {cont_vint}')
if cont_dez > 0:
    print(f'Cédulas de R$10: {cont_dez}')
if cont_um > 0:
    print(f'Cédulas de R$1: {cont_um}')
