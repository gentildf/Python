#Desafio 004 "Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.
n = input('Digite um valor a ser analisado: ')
print('O valor inserido é: ', type(n))
print('Ele é numérico?', n.isnumeric())
print('Ele é alfabeto?', n.isalpha())
print('Ele é alfanumérico?', n.isalnum())
print('Ele está em caixa alta?', n.isupper())
print('Ele está em minusculo?', n.islower())
