# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM ºC E CONVERTA PARA ºF

temperatura = float(input('Informe a temperatura em ºC: '))
conversao = temperatura * 1.8 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(temperatura, conversao))
