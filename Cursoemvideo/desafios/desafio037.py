"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário.
- 2 para octal.
- 3 para hexadecimal.

"""

num = int(input('\033[4mDigite o número que deseja transformar:\033[m '))
opc = int(input('\033[32mEscolhe a base que deseja que seja convertida:\033[33m\n'
                '1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\n\033[32m'
                'Digite o número referente a opção:\033[m '))
if opc == 1:
    print('O número \033[33m{}\033[m convertido para binário fica \033[33m{}\033[m.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O número \033[33m{}\033[m convertido para octal fica \033[33m{}\033[m.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O número \033[33m{}\033[m convertido para hexadecimal fica \033[33m{}\033[m.'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mVOCÊ DIGITOU UMA OPÇÃO INEXISTENTE, FAVOR REFAÇA A OPERAÇÃO.')
