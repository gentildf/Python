#Desafio 006 = "Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input("Digite um número: "))
print("O dobro de \033[33m{0}\033[m é \033[31m{1}\033[m.\n"
      "O triplo de \033[33m{0}\033[m é \033[31m{2}\033[m.\n"
      "A raiz quadrada de \033[33m{0}\033[m é \033[31m{3:.2f}\033[m."
      .format(n, (n*2), (n*3), (n**(1/2))))