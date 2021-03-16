"""
Refaça o desáfio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
"""
reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
lista = [reta1, reta2, reta3]
lista.sort()
if lista[1] + lista[0] > lista[-1]:
    print('\033[32mAs três retas podem formar um triângulo.\033[m')
    if reta1 == reta2 == reta3:
        print('Esse triângulo é do tipo \033[4mEQUILÁTERO\033[m.')
    elif (reta1 == reta2 != reta3) or (reta2 == reta3 != reta1) or (reta3 == reta1 != reta2):
        print('Esse triângulo é do tipo \033[4mISÓSCELES\033[m.')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('Esse triângulo é do tipo \033[4mESCALENO\033[m.')
else:
    print('\033[31mAs três retas não podem formar um triângulo.\n'
          'Motivo: \033[33m{}m\033[m + \033[33m{}m\033[m não é maior que \033[33m{}m\033[m'
          .format(lista[0], lista[1], lista[-1]))

