"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.

"""
somaidade = 0
maior = 0
count = 0
maisvelho = ''
oldage = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if idade > maior and sexo in 'Mm':
        maisvelho = nome
        oldage = idade
    if sexo == 'F' and idade < 20:
        count += 1

mediaidade = somaidade / 4
print('A média de idade é de {}.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {}'.format(maisvelho, oldage ))
print('{} mulheres tem menos de 20 anos.'.format(count))
