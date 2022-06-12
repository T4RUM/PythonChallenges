# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

ano = int(input('Em qual ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print(f'Com {idade} anos, você pertence a categoria MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos, você pertence a categoria INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos você pertence a categoria JUNIOR.')
elif idade <= 25:
    print(f'Com {idade} anos você pertence a categoria SÊNIOR.')
elif idade > 25:
    print(f'Com {idade} anos você pertence a categoria MASTER.')
