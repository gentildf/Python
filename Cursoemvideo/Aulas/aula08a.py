# Aula sobre módulos do Python
# comando 'import' traz módulos ou bibliotecas.
#Exemplo 1: "import biblioteca/modulo"
#Exemplo 2: "from biblioteca/modulo import funcionalidade"

#funcionalidades da biblioteca/modulo 'math'
#ceil  = Arrendonda para cima
#floor = Arredonda para baixo
#trunc = Trunca, ou seja, elimina tudo depois
#pow = potencia
#sqrt = Raiz quadrada
#factorial = Calculo de fatorial
#------------------------------
#import math
#from math import sqrt,ceil
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz quadrada de {} é igual a {}'.format(num, ceil(raiz)))
#-----------------------------------------------------------------------
#import random
#n = random.randint(1, 10)
#print(n)
# --------------------------------------------------------------------------
import emoji
print(emoji.emojize("Olá mundo! :sunglasses::earth_americas:", use_aliases=True))



