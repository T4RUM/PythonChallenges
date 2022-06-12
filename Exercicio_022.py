# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE :
# O NOME COM TODAS AS LETRAS MAIUSCULAS
# O NOME COM TODAS AS LETRAS MINUSCULAS
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
