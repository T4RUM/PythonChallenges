#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR.
# CONSEIDERE US$ 1,00 = R$ 3,27


carteira = float(input('Quantos reais você tem na carteira? '))
dolar = float(5.18)
resulado = carteira / dolar
print('Com R${} você pode comprar US${:.2F}'.format(carteira, resulado))
