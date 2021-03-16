"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cade valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
"""
while True:
    num = int(input('Digite o número para mostrar a sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        m = c * num
        print(f' {num} x {c} = {m} ')
    d = str(input('Deseja digitar outro número? [S / N]: ')).upper()[0]
    if d in 'N':
        break
print('Sessão finalizada com sucesso.')
