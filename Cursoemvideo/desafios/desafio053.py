"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""
frase = str(input('Digite uma frase: '))
separado = frase.split()
junto = ''.join(separado)
contrario = junto[::-1]
#frase1.split()
if junto == contrario:
    print('A frase é do tipo palíndromo!')
else:
    print('A frase não é do tipo palíndromo.')
print('{}'.format(junto))
print('{}'.format(contrario))
"""
-----------------------------------------
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] # Vai adicionando (a+b+c) = abc

Nesse caso o 'len(junto) -1' ta trazendo total de casas -1 (por conta do numero final nao ser igual a quantidade.)
o -1 é para dizer que vai começar do ultimo antes do zero.
o -1 tereiro é para dizer como será feito o tratamento. 
-----------------------------------------"""