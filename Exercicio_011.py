# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M QUADRADOS

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = float(altura * largura)
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area))
print('A quantidade de tinta necessaria é = {:.2F} Litros'.format(tinta))
