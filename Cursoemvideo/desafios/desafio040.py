"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- Média abaixo de 5.0:
REPROVADO.
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO.
"""
print(('\033[1m<\033[m' * 6) + ' \033[35mSISTEMA DE VERIFICAÇÃO DE MÉDIA PARA APROVAÇÃO ' + (6 * '\033[1m>\033[m'))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Você obteve média de \033[1;33m{:.1f}\033[m e está \033[1;31mREPROVADO\033[m.'.format(media))
elif 6.9 >= media >= 5.0:
    print('Você obteve média de \033[1;33m{:.1f}\033[m e está de \033[1;33mRECUPERAÇÃO\033[m!'.format(media))
else:
    print('Você obteve média de \033[1;33m{:.1f}\033[m e \033[1;32mPARABÉNS\033[m você \033[1;32mPASSOU\033[m.'
          .format(media))
