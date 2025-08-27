print('-'*30)
print('    LOJA SUPER BARATÃO    ')
print('-'*30)
continuar = 's'
total = 0
produto_caro = 0
barato = ''
cont = 0
menor = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total = total + preco
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        produto_caro = produto_caro+1
    continuar = input('Quer continuar? [S/N] ').lower()
    if continuar == 'n':
        break
print('-'*15, ' FIM DO PROGRAMA ', '-'*15)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {produto_caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

