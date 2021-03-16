#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
t = float(input('\033[4mDigite a temperatura em Celsius:\033[m '))
#A formula para conversão é = ((C * 9) / 5) + 32 = F
f = (t*9/5)+32
print('\033[33mA temperatura em Fahrenheit é de:\033[m \033[1m{}ºF\033[m'.format(f))

