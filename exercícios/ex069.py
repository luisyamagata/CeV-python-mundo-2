continuar = 's'
maiores = 0
homens = 0
mul_novas = 0
while continuar == 's':
    print('-' * 30)
    print('    CADASTRE UMA PESSOA    ')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    sexo = input('Sexo: [M/F] ').lower()
    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        mul_novas += 1
    continuar = input('Quer continuar? [S/N]').lower()

if continuar == 'n':
    print('='*7, ' FIM DO PROGRAMA', '='*7)
    print(f'Total de pessoas com mais de 18 anos: {maiores}')
    print(f'Ao todo temos {homens} homens cadastrados.')
    print(f'E temos {mul_novas} mulheres com menos de 20 anos.')


