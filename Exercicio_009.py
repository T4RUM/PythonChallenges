#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA

#=====================================================================================#
# VARIAVEL PARA PEGAR O NUMERO DA TABUADA
# CRIAR UM RANGE DE 0 A 11 (0 A 10)
# PERCORRER ESSE RANGE FAZENDO A MULTIPLICAÇÃO E ARMAZENAR EM UMA VARIAVEL
# DAR UM PRINT EM TODAS AS VARIAVEIS MONTANDO O RESULTADO (I , RESULTADO , NUMERO )

numero = int(input('Digite um número para ver sua tabuada: '))

for i in range(0,11):
    resultado = numero * i
    print(numero, '*', i, '=', resultado)

