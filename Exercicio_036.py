# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
# O PROGRAMA VAI PERGUNTAR O VALOR DA CASA
# O SALÁRIO DO COMPRADOR
# E EM QUANTOS ANOS ELE VAI PAGAR
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABEMOS QUE ELA NÇAO PODE EXCEDER 30% DO SALARIO OU ENTÃO O EMPRESTIMO SERA NEGADO

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento?  '))
prestação = casa / (anos * 12)
mínimo = salario * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')