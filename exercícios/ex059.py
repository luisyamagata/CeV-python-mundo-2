num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''' )
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é: {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'O produto de {num1} e {num2} é: {mult}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}.')
        elif num2 > num1:
            print(f'{num2} é maior que {num1}.')
        else:
            print('{num1} é igual a {num2}.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente.')
print('Fim do programa! Volte Sempre!')
