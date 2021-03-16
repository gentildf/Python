"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""
c = 0  # Variavel de contagem de quantos números foram inseridos.
n = 1  # Variavel de quantidade de números a inserir.
m = 0  # Variavel de média
num = 0
num1 = 0
maior = 0
menor = 0
while n != 0:
    c += 1
    n -= 1
    num = int(input('Insira um número inteiro: '))
    if n == 0:
        n = int(input('Deseja continuar a inserir números?'
                      '\n Se não, digite 0.'
                      '\n Se sim, digite a quantidade: '))
    if num >= maior:
        maior = num
    if num != 0 and menor == 0:
        menor = num
    if num <= menor:
        menor = num
    num1 += num
m = num1 / c
print('A média de todos números inseridos foi de {}.'.format(m))
print('O maior número inserido foi {}.'.format(maior))
print('O menor número inserido foi {}.'.format(menor))
