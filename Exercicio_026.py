# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# QUANTAS VEZES APARECE A LETRA "A"
# EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
# EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.


frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes na frase. '.format(frase.count('a')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))

