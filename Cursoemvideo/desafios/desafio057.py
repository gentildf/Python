"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Digite qual seu sexo [M]/[F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': # Tambem poderia usar "while sexo not in "MF" "
    print('Você digitou uma opção invalida!')
    sexo = str(input('Digite qual seu sexo [M]/[F]: ')).strip().upper()[0]
print('Seu sexo é {}'.format(sexo))
