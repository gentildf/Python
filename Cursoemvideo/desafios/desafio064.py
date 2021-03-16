"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
"""
n = c = t = 0
while n != 999:
    c += 1
    n = int(input('Digite um número para destravar a repetição: '))
    t += n  # Calculo para soma de todos os números antes de destravar a repetição.
print('Sequencia destravada.')
print('A quantidade de números inseridos até destravar foi de {}.'.format(c - 1))
print('Os números digitados somado dão {}.'.format(t - 999))
