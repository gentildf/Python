#Desafio 005 = " Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro: '))
print('O antecessor de \033[30m{0}\033[m é \033[30m{1}\033[m. \n'
      'O sucessor de \033[30m{0}\033[m é \033[30m{2}\033[m. '.format(n, (n-1), (n+1)))
