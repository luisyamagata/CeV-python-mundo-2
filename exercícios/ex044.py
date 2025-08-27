print('===== LOJAS POMBO =====')
produto = int(input('Preço das Commpras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
forma = int(input('Qual é a opção? '))
if forma == 1:
    produto2 = (produto * 0.9)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, produto2))
elif forma == 2:
    produto2 = (produto * 0.95)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, produto2))
elif forma == 3:
    parcela = (produto / 2)
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, produto))
elif forma == 4:
    qparcelas = int((input('Quantas parcelas? ')))
    produto3 = (produto *1.2)
    parcela4 = (produto3/qparcelas)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qparcelas, parcela4))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, produto3))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
