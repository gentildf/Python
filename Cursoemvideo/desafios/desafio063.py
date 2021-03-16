"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos ed uma Sequência de Fibonacci.
"""
'''a + a + b + c
a + a = b
a + b = c 
b + c = d '''
print('>>>>> SEQUENCIA DE FIBONACCI <<<<<')
n = int(input('Digite um número: ')) # Número inteiro a ser recebido.
e = int(input('Digite quantos elementos deseja ver: ')) # Quantidade de elementos.
c = 0 # Contador.
f = 0 # Fibonacci
while c != e: #Contador comça com 0 e vai até o e ( com o c+= 1 )
    c += 1 # Contagem de while
    print('{}>'.format(f), end='')
    f = f + n
    n = f - n
    if n == 0:
        n + 1
