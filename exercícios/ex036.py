v = float(input('Valor da casa: '))
s = float(input('Salário do comprador: '))
a = int(input('Quantos anos de financiamento? '))
prestmax = s * 0.3
parcelamensal = v / (a*12)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(v, a), end='')
print('a prestação será de R${:.2f}'.format(parcelamensal))
if parcelamensal <= prestmax:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
