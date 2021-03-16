#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por Km rodado.
km = float(input('\033[7;33mDigite a quantidade de km rodado: '))
dias = int(input('Digite a quantidade de dias usado: \033[m'))
totalkm = km * 0.15
totaldia = dias * 60
print('-'*30, ' \n'
      'O total a pagar é de: \033[32mR${:.2f}\033[m.\n'
      'Consumo de Km total: \033[32mR${:.2f}\033[m.\n'
      'Consumo de dias total: \033[32mR${:.2f}\033[m.\n'
      .format((totalkm+totaldia), totalkm, totaldia)
      + '-' * 30)
