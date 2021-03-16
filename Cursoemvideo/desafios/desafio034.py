'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superioes a R$1.250,00, calcule um aumento de 10%
Para inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite seu salário: R$'))
if salario <= 1250:
    aumento = (salario*15/100)+salario
    porc = 15
else:
    aumento = (salario*10/100)+salario
    porc = 10
print('O salário recebeu um aumento de '
      '\033[1;32m{}%\033[m e \033[4matualizado\033[m ficou no valor de: \033[1;32mR${:.2f}\033[m'
      .format(porc, aumento))
