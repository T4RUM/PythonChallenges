# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensgem:
# - O primeiro valor é maior
# - O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
elif n2 == n1:
    print(f'{n1} é igual a {n2}')