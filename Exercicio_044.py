
print('''
 _       _____       _       ___   _____            ___  ___   _   _   _____        ___   _____  
| |     /  _  \     | |     /   | /  ___/          /   |/   | | | | | |  _  \      /   | |_   _| 
| |     | | | |     | |    / /| | | |___          / /|   /| | | | | | | |_| |     / /| |   | |   
| |     | | | |  _  | |   / / | | \___  \        / / |__/ | | | | | | |  _  /    / / | |   | |   
| |___  | |_| | | |_| |  / /  | |  ___| |       / /       | | | |_| | | | \ \   / /  | |   | |   
|_____| \_____/ \_____/ /_/   |_| /_____/      /_/        |_| \_____/ |_|  \_\ /_/   |_|   |_|   ''')
preco = float(input('Qual o valor do produto? R$ '))
print('='*35)
print('=    QUAL FORMA DE PAGAMENTO?    =')
print('='*35)
print('1) DINHEIRO\n2) CHEQUE\n3) CARTÃO')
forma_de_pagamento = int(input(''))

if forma_de_pagamento == 1:
    print('O valor da sua compra com 10% de Desconto ficara R$ {}'.format(preco-(preco * 10)/100))
elif forma_de_pagamento == 2:
    print('O valor da sua compra com 10% de Desconto ficara R$ {}'.format(preco - (preco * 10) / 100))
elif forma_de_pagamento == 3:
    print('='*35)
    print('=    EM QUANTAS VEZES NO CARTÃO?  =')
    print('=' * 35)
    print('1) A VISTA\n2) 2X NO CARTÃO\n3) 3X OU MAIS NO CARTÃO')
    cartao = int(input(''))
    if cartao == 1:
        print('O valor da sua compra a VISTA teve 5% de desconto e ficou R$ {}'.format(preco-(preco * 5)/100))
    elif cartao == 2:
        print('O valor da sua compra em 2X no CARTÃO ficou R$ {} SEM DESCONTOS'.format(preco))
    elif cartao == 3:
        print('O valor da sua compra em 3X OU MAIS NO CARTÃO teve 20% de JUROS e ficou R$ {}'.format(preco+(preco * 20)/100))
