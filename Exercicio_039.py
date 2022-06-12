# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - ano

if idade < 18:
    print(f'Você deve se alistar no serviço militar daqui a {18-idade} anos.')
elif idade == 18:
    print(f'Você deve se alistar no serviço militar esse ano!')
elif idade > 18:
    print(f'Você ja devia ter se alistado a {idade - 18} anos atras!')
    print('''
               _______________________
              (<$$$$$$$>######<::::::>)
            ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~ ~
          ~                                ~
        .~                                   ~
    ()\/_____                           _____\/()
   .-''      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-.
.-~              __________________              ~-.
`~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~'
| | | #### #### || | | | [] | | | || #### #### | | |
;__\|___________|++++++++++++++++++|___________|/__;
 (~~====___________________________________====~~~)
  \------_________[SERVIÇO MILITAR]________-------/
     |      ||         ~~~~~~~~       ||      |
      \_____/                          \_____/''')