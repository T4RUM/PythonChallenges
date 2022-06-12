# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVAOD

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média foi {media}: REPROVADO')
elif media > 5.0 and media < 6.9:
    print(f'Sua média foi {media}: RECUPERAÇÂO')
else:
    print(f'Sua média foi {media}: APROVADO!!!')