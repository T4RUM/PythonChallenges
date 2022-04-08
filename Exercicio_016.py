# CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
# EX: DIGITE UM NÚMERO: 6.127
# O NÚMERO 6.127 TEM A PARTE INTEIRA 6

import math
num = float(input('Digite um valor: '))
resultado = math.trunc(num)
print('A parte inteira do número que você escolheu é: {}'.format(resultado))