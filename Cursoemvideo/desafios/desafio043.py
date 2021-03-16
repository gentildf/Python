"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo de peso.
- Entre 18.5 e 25: Peso ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade mórbida.
"""
print('Sistema de calculo de IMC')
altura = float(input('Digite a altura \033[32m(ao invés de , use o .)\033[m : '))
peso = float(input('Digite seu peso \033[32m(ao invés de , use o .)\033[m : '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está com o IMC de {:.2f}, seu indice é \033[1;31mABAIXO DO PESO\033[m.'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está com o IMC de {:.2f}, seu indice é \033[1;32mPESO IDEAL\033[m.'.format(imc))
elif 25. <= imc < 30:
    print('Você está com o IMC de {:.2f}, seu indice é \033[1;33mSOBREPESO\033[m.'.format(imc))
elif 30 <= imc < 40:
    print('Você está com o IMC de {:.2f}, seu indice é \033[1;33mOBESIDADE\033[m.'.format(imc))
elif imc > 40:
    print('Você está com o IMC de {:.2f}, seu indice é \033[1;31mOBESIDADE MORBIDA\033[m.'.format(imc))