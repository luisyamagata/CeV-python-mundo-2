from datetime import date
nasc = int(input('Ano de nascimento? '))
ano = date.today().year
idade = ano-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))
if idade < 18:
    saldo = 18 - idade
    anoalis = nasc + 18
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(anoalis))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    anoalis = nasc + 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}.'.format(anoalis))
