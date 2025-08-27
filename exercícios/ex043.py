p = float((input('Qual o seu peso? (Kg) ')))
a = float((input('Qual é a sua altura? (m) ')))
imc = p/(a ** 2)
print('O IMC dessa éssoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 25 > imc >= 18.5:
    print('PARABÉNS, Você está na faixa de PESO NORMAL.')
elif 30 > imc >= 25:
    print('Você está em SOBREPESO')
elif 40 > imc >=30:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
