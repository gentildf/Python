nome = str(input('Qual é o seu nome? '))
if nome == 'Denis':
    print('Que nome lindo!')
elif nome == 'Joao' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é comum demais.')
elif nome in 'Ana, Julia, Mariana, Julia':
    print('Seu nome é lindo demais!')
print('Tenha um ótimo dia, {}.'.format(nome))