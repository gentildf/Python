"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 < num2:
    print('O número \033[33m{}\033[m é maior que o número \033[33m{}\033[m.'.format(num2, num1))
elif num1 > num2:
    print('O número \033[33m{}\033[m é maior que o número \033[33m{}\033[m'.format(num1, num2))
else:
    print('Os dois números informados são \033[33mIGUAIS\033[m.')