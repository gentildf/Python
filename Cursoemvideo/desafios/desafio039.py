"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Se programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
print(('\033[1;32m|^|\033[m'*4)+' \033[2;34mVERIFICADOR DE ALISMENTO MILITAR\033[m '+(4*'\033[1;32m|^|\033[m'))
print('\033[31mA idade para alistamento é de 18 anos.\033[m')
nasc = int(input('\033[4;35mInforme o ano de nascimento:\033[m '))
ano = date.today().year
idade = ano - nasc
sexo = int(input('''Qual é o seu sexo?
[ 1 ] MASCULINO
[ 2 ] FEMININO
Digite o número referente:  '''))
if sexo == 1:
    if idade < 18:
        print('Você ainda \033[1;31mNÃO\033[m pode se alistar,.')
        print('Faltam {} anos para você se alistar.'.format(18-idade))
    elif idade == 18:
        print('Esse ano você fez ou irá fazer 18 anos.')
        print('\033[1;31mVocê deve se alistar.\033[m')
    else:
        print('\033[31mVocê ja passou do prazo para alistamento.\033[m')
        print('Fazem {} anos do prazo de alistamento.'.format(idade - 18))
else:
    print('Você não pode ser alistar.')