termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 0
max = 10
while max != 0:
    while cont != max:
        termo = termo + razao
        print('{} > '.format(termo), end='')
        cont += 1
    print('PAUSA')
    max = int(input('\nPara mais termos, digite o número que quer ver: '))
    cont = 0
'''while cont != (max - 1):
    termo = termo + razao
    print('{}>'.format(termo), end='')
    cont += 1
max = int(input('\nPara mais termos, digite o número que quer ver: '))'''
print('\nOperação finalizada.')