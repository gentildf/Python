"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidos.
"""
maior = 0
menor = 0
for c in range(1, 6):
    kg = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg

print('O maior peso é de {}Kg.'.format(maior))
print('O menor peso é de {}Kg.'.format(menor))
