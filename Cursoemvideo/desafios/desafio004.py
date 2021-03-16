#Desafio 004 "Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.
n = input('Digite um valor a ser analisado: ')
print('\033[30mO valor inserido é do tipo: ', type(n))
print('\033[33mEle é numérico?', n.isnumeric())
print('\033[31mEle é alfabeto?', n.isalpha())
print('\033[32mEle é alfanumérico?', n.isalnum())
print('\033[34mEle está em caixa alta?', n.isupper())
print('\033[32mEle está em minusculo?', n.islower())
