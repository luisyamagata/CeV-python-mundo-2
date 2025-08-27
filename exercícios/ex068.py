from random import randint
game_over = False
sequencia_jogador = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
while game_over == False:

    num_jogador = int(input('Diga um valor: '))
    esc_jogador = input('Par ou Ímpar? [P/I] ').upper()
    num_cpu = randint(1, 10)
    soma = num_jogador + num_cpu
    if esc_jogador == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {num_jogador} e o computador {num_cpu}. Total de {soma}. DEU PAR')
            print('Você VENCEU!')
            sequencia_jogador = sequencia_jogador + 1
        elif soma % 2 > 0:
            print(f'Você jogou {num_jogador} e o computador {num_cpu}. Total de {soma}. DEU ÍMPAR')
            print('Você perdeu.')
            game_over = True
    if esc_jogador == 'I':
        if soma % 2 > 0:
            print(f'Você jogou {num_jogador} e o computador {num_cpu}. Total de {soma}. DEU ÍMPAR')
            print('Você VENCEU!')
            sequencia_jogador = sequencia_jogador + 1
        elif soma % 2 == 0:
            print(f'Você jogou {num_jogador} e o computador {num_cpu}. Total de {soma}. DEU PAR')
            print('Você perdeu.')
            game_over = True
print(f'GAME OVER! Você venceu {sequencia_jogador} vezes.')

