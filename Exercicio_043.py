# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideial
# - 25 até 30: Sobrepesso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida


altura = float(input('Qual é sua altura (m) ? '))
peso = float(input('Qual é seu peso (Kg) '))
imc = peso / (altura*altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc <= 18.5:
        print('Você esta ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('Você esta com PESO NORMAL')
elif imc > 25 and imc <= 30:
    print('Você esta com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você esta com OBESIDADE')
else:
    print('Você esta com OBESIDADE MÓRBIDA')