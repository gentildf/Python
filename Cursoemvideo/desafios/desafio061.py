"""
Refaça p DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
"""
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 0
print(termo, end='')
while cont != 10:
    termo = termo + razao
    print('>{}'.format(termo), end='')
    cont += 1
