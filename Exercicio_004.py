# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE.


texto = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(texto))
print('Só tem espaços? (', texto.isspace(),')')
print('É um número? (', texto.isnumeric(),')')
print('É alfabético? (', texto.isalpha(),')')
print('É alfanumérico? (', texto.isalnum(),')')
print('Está em maiúsculas? (', texto.isupper(),')')
print('Está em minúsculas? (', texto.islower(),')')
print('Está capitalizada? (', texto.istitle(),')')

