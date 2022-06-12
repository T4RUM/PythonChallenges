# ESCREVE UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80 KM/H, MOSTRA UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMETE

velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('Tenha um bom dia! Dirija com segurança !')
else:
    print('''MULTADO! Você excedeu o limite permitido que é de 80Km/h
    Você deve pagar uma multa de R$: {}'''.format(multa))

