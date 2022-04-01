# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO


salario = float(input('Qual o seu salário? '))
aumento = float(input('Qual a porcentagem do seu aumento? '))
reajuste = (salario * aumento) / 100
holerite = salario + reajuste
print('O seu salario teve um reajuste de {:.0F}% e agora é R${:.2F}'.format(aumento, holerite))
