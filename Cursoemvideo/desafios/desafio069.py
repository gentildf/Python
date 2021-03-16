"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostrar:
- Quantas pessoas tem mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.
"""
sex = ' '
age = c = h = f = 0
while True:
    while sex != 'M' and sex != 'F':
        sex = str(input('SEXO [M/F]: ')).upper()[0]  # INPUT DE SEXO
    while True:
        age = int(input('IDADE: '))  # INPUT DE IDADE
        if 0 < age < 200:
            break
    if age >= 18:
        c += 1
    if sex == 'M':
        h += 1
    elif sex == 'F':
        if age < 20:
            f += 1
    quest = str(input('Deseja continuar a inserir? [S/N]:')).upper()[0]
    if quest == 'N':
        break
    sex = 'none'
print(f'Número de pessoas maiores de 18 anos: {c}')
print(f'Número de homens cadastrados: {h}')
print(f'Número de mulheres com menos de 20 anos: {f}')
