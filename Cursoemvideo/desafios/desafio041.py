"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JUNIOR.
- Até 25 anos: SÊNIOR.
- Acima: MATER.
"""
from datetime import date
print('\033[1;32mPROGRAMA DE AUTENTICAÇÃO DE CATEGORIA DA CNN\033[m')
ano_atual = date.today().year
ano_info = int(input('Informe em que ano o atleta nasceu: '))
categ = ano_atual - ano_info
if categ <= 9:
    print('O atleta pertence a categoria \033[mMIRIM\033[m.')
elif categ <= 14:
    print('O atleta pertence a categoria \033[mINFANTIL\033[m.')
elif categ <= 19:
    print('O atleta pertence a categoria \033[mJUNIOR\033[m.')
elif categ <= 25:
    print('O atleta pertence a categoria \033[mSÊNIOR\033[m.')
else:
    print('O atleta pertence a categoria \033[mMASTER\033[m.')
