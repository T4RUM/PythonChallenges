# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR EM UM NÚMERO INTEIRO ENTRE 0 A 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USÚARIO VENCEU OU PERDER

import random
numero = [1, 2, 3, 4, 5]
sorteio = random.choice(numero)
jogador = int(input('Advinhe o numero que o computador escolheu entre 0 a 5: '))
if jogador == sorteio:
    print('Parabens você acertou o numero')
else:
    print('Você errou, tente novamente.')