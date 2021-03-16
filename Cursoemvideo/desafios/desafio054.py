"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Considerar maioridade como 21.
"""
from datetime import date
maior = 0
menor = 0
print('Digite a seguir o ano de nascimento de sete pessoas: ')
for c in range(0, 7):
    ano_nasc = int(input('DIGITE O ANO DE NASCIMENTO: '))
    ano = date.today().year - ano_nasc
    if ano >= 21:
        maior += 1
    else:
        menor += 1
print("""As informações de ano de nascimento das sete pessoas retornaram:
{} são maiores de idade.
{} são menores de idade.""".format(maior, menor))
