# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# 1 PARA BINÁRIO
# 2 PARA OCTAL
# 3 PARA HEXADECIMAL


numero = int(input('Digite um número: '))

print('Escolha uma das opções de conversão:')
print(' [ 1 ]  Para converter para Binário')
print(' [ 2 ]  Para converter para Octal')
print(' [ 3 ]  Para converter para Hexadecimal')

conversao = int(input(''))

if conversao == 1:
    print(f'O número {numero} convertido para Binário é = {bin(numero)[2:]}')
elif conversao == 2:
    print(f'O número {numero} convertido para Octal é = {oct(numero)[2:]}')
elif conversao == 3:
    print(f'O número {numero} convertido para Hexadecimal é = {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
