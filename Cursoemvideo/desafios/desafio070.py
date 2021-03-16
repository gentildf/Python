"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostrar:
- Qual é o total gasto na compra.
- Quantos produtos custam mais de R$1000.
- Qual é o nome do produto mais barato.
"""
total = caro = cont = barato = 0
barato_n = ''
while True:
    name = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = preco
    elif preco < barato:
        barato = preco
        barato_n = name
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Deseja inserir mais? [S/N]: ')).upper()[0]
    if quest == 'N':
        break
print(f'Total de compra: R$\033[m{total:.2f}\033[m')
print(f'Quantidade de produtos acima de R$1000,00: \033[m{caro}\033[m.')
print(f'Produto mais barato: {barato_n}.\nCustando: R$\033[m{barato:.2f}\033[m')
