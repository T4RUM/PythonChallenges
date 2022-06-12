# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

import random
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
sorteio = random.choices([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado para apagar a lousa foi: {}'. format(sorteio))



# OUTRO MODO DE SE FAZER ISSO POREM DE MANEIRA QUE FICA FIXO OS NOMES
'''const = ['Wesley','Marcos', 'Ricardo', 'João']'''
'''sorteio = random.choice(const)'''
