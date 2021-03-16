#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('\033[33mVerificando se o nome \033[32m{}\033[33m possui "\033[31mSILVA\033[33m"'.format(nome))
print("\033[1;31mSILVA\033[m" in nome.upper())



