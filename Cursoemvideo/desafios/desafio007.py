#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A média total das duas notas é \033[31m{:.1f}\033[m'.format((n1+n2)/2))
