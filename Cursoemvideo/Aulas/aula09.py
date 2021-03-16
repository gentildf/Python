"""Manipulando cadeias de caracteres (texto)
O que chamamos de frase, o python chama de cadeira de texto.
-----------------
Fatiamento
frase = "C u r s o   e m   V  í  d  e  o    P  y  t  h  o  n
         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
frase=[9:13]  (Lembrar que o 13 não será incluido)
resultado: "Vide"

frase=[9:21:2]   - Vai pular de 2 em 2 (mostrando o segundo).
(lembrar que foi colocado o 21 pois funciona, ele não é incluido no print)

frase=[:5]      - Vai até o 4.

frase=[15:]     -Começa do 15 até o final.

frase[9::3]     -Começa do 9 até o final pulando de 3 em 3 (mostrando o terceiro).
---------------------------------------------------------
Analise
função len:
len significa "comprimento"
len(frase) é igual a 21 caracteres.

Função de contagem:
frase.count('o') Conta quantas vezes tem o caracter 'o'.

frase.count('o', 0, 13) Conta de 0 a 12 quantos 'o' tem.

função de procurar:
frase.find('deo')  vai indicar onde começa == 11.

frase.find('Android')  Retorna -1. Significa que não foi encontrado.

Operador in
'Curso' in frase      Retorna "True".

Transformação:
frase.replace('Python','Android')   Troca uma palavra pela outra. No caso, o Python pela palavra Android.

frase.upper()       O que ja for maisculo ele mantém e o que não for ele torna maiusculas.
frase.lower()       Contrário do upper.
frase.capitalize()  Pega tudo e deixa a primeira letra em maiuscula e as demais em minusculas.
frase.title()       Parecido com o capitalize, porém ele pega de cada palavra na frase, considerando o ' ' uma quebra.
frase.strip()       Remove todos os espaços inuteis, tanto no inicio quanto no final.
frase.rstrip()      Remove os da direita.
frase.lstrip()      Remove os da esquerda.
-------------------------------------------------------------
Divisão
frase.split()       Divide(cada uma recebe um novo indice), considerando os espaços.(dar uma lida sobre e testar)

Junção
'-'.join(frase)     Mostra juntos e coloca um traço entre eles.

"""
