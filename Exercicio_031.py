# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200KM
# R$ 0,45 PARA VIAGENS MAIS LONGAS


distancia = int(input('Qual distanciada sua viagem? '))
valor1 = float(0.50)
valor2 = float(0.45)
if distancia <= 200:
    print('O valor da passagem é de R${} por {}Km percorrido'.format(valor1*distancia, distancia))
else:
    print('O valor da passagem é de R${} por {}Km percorrido'.format(valor2*distancia, distancia))