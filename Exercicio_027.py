# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
# EX: ANA MARIA DE SOUZA
# PRIMEIRO = ANA
# ÚLTIMO = SOUZA

nome = str(input('Digite o seu nome completo: ')).strip()
separador = nome.split()
print('Muito prazer em te conhecer !')
print('Seu primeiro nome é {}'.format(separador[0]))
print('Seu ultimo nome é {}'.format(separador[len(separador)-1]))
