# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO
# MOSTRE O SEU NOVO PREÇO COM 5% DE DESCONTO

preco = float(input('Qual é o preço do produto? R$ '))
porcentagem = int(input('Quantos porcentos de Desconto: '))
desconto = (preco * porcentagem) / 100
resultado = preco - desconto
print('O produto com {}% de desconto vai custar R$: {:.2F}'.format(porcentagem, resultado))
