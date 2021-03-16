#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n = float(input('\033[32mDigite o numero:\033[m'))
print('O número digitado é \033[33m{0:.0f}m\033[m.\n'
      'Ele apresentado em centimetros fica \033[33m{0:.2f}cm\033[m.\n'
      'Apresentado em milímetros fica \033[33m{0:.3f}mm\033[m'
      .format(n))
#print('O número em metros é {0}.\n
# O número em convertido para centimetros é {1}.\n
# O número convertido para milimetros é {2}'
# .format(n, n/100, n/1000))
