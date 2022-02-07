# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.

n1 = int(input('Digite um numero: '))
antecessor = n1 - 1
sucessor = n1 + 1
print('''Antecessor do numero {} é: {}
E o sucessor é: {}'''.format(n1, antecessor, sucessor))



#UTILIZANDO MENOS MEMORIA
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é  {}'.format(n, (n-1), (n+1)))

