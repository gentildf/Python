#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''num = str(input('Digite um número de 0 a 9999: '))
print(
    'O número: {} está dividido entre as casas:\n'
    'unidade: {}\n'
    'dezena: {}\n'
    'centena: {}\n'
    'milhar: {}\n'.format(num, num[3], num[2], num[1], num[0])
    )
'''
num = int(input('Digite um número de 0 a 9999: '))
n = int(num)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(
    '\033[4;35mO número: \033[31m{}\033[4;35m está dividido entre as casas:\033[m\n'
    'unidade: \033[31m{}\033[m\n'
    'dezena: \033[31m{}\033[m\n'
    'centena: \033[31m{}\033[m\n'
    'milhar: \033[31m{}\033[m\n'.format(num, u, d, c, m)
    )

