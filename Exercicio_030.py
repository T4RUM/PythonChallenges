# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPART

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 1:
    print('O numero {} é Impar'.format(numero))
else:
    print('O numero {} é Par'.format(numero))
