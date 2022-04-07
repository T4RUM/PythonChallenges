# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
# CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO


dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
c1 = 60 * dias
c2 = 0.15 * km
resultado = c1 + c2
print('O total a pagar é de R${:.2f}'.format(resultado))

















'''pago = (dias * 60) + (km * 0.15)'''