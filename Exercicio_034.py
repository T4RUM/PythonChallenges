# EXCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1.250,00 CALCULE UM AUMENTO DE 10%
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%


salario = float(input('Qual o salário do funcionário? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

