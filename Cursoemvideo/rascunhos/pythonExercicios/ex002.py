#Exercicio 002
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. (Até a aula 04)

name = input("Qual seu nome? ")
print('Seja bem vindo', name+'.')


# Tem outro modo também para formatação: usando o {}
# ex: print('Seja bem vindo {}!'.format(name))
# Onde o {} irá pegar a formatação da variavel name e colocar dentro do ''
#Testando:
print('Seu nome é {}!'.format(name))

