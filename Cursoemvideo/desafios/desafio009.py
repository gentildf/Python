#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite o número: '))
print('\033[31m-=-\033[m'*12)
print('\033[7;30mA tabuada de {0} é:\033[m\n'
      '0 x {0:2} = {1}\n'
      '1 x {0:2} = {2}\n'
      '2 x {0:2} = {3}\n'
      '3 x {0:2} = {4}\n'
      '4 x {0:2} = {5}\n'
      '5 x {0:2} = {6}\n'
      '6 x {0:2} = {7}\n'
      '7 x {0:2} = {8}\n'
      '8 x {0:2} = {9}\n'
      '9 x {0:2} = {10}\n'
      '10 x {0:1} = {11}'
      .format(n,n*0, n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10)
            )
print('\033[31m-=-\033[m'*12)
