import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')


sorteio = random.sample([aluno1,aluno2,aluno3,aluno4],k=4)
print('A ordem do sorteio foi: {}'.format(sorteio))

'''
from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))

lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

'''