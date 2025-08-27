from datetime import date
nasc = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade > 25:
    print('Classificação: MASTER')
elif idade <= 25 and idade > 19:
    print('Classificação: SÊNIOR')
elif idade <= 19 and idade > 14:
    print('Classificação: JÚNIOR')
elif idade <= 14 and idade > 9:
    print('Classificação: INFANTIL')
elif idade <= 9:
    print('Classificação: MIRIM')
