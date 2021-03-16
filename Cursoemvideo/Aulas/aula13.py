"""
Estrutura de repetições (Laçoes de repetição)
"""
for c in range(0,6):
    print('Oi')
print('FIM')
"""
for c in range(0, 6, -1)  -> A ultima casa é como será feito a iteração, no caso será 6 - 1.
                                                         se fosse 2 seria a cada duas casas.
"""
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')