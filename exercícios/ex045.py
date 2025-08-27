from random import randint
from time import sleep
print('Vamos jogar jokenpô!')
print('''Suas opções:
[ 0 ] para PEDRA
[ 1 ] para PAPEL
[ 2 ] para TESOURA
      ''')
escolhajogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
escolhacpu = (randint(0,2))
print('-='*13)
if escolhacpu == 0:
    print('Computador jogou Pedra')
elif escolhacpu == 1:
    print('Computador jogou Papel')
elif escolhacpu == 2:
    print('Computador jogou Tesoura')
if escolhajogador == 0:
    print('Jogador jogou Pedra')
elif escolhajogador == 1:
    print('Jogador jogou Papel')
elif escolhajogador == 2:
    print('Jogador jogou Tesoura')
else:
    print('Opção inválida. Tente novamente!')
print('-='*13)
if escolhacpu == escolhajogador:
    print('EMPATE')
elif escolhajogador == 0 and escolhacpu == 2:
    print('JOGADOR VENCE')
elif escolhajogador == 1 and escolhacpu == 0:
    print('JOGADOR VENCE')
elif escolhajogador == 2 and escolhacpu == 1:
    print('JOGADOR VENCE')
elif escolhacpu == 0 and escolhajogador == 2:
    print('COMPUTADOR VENCE')
elif escolhacpu == 1 and escolhajogador == 0:
    print('COMPUTADOR VENCE')
elif escolhacpu == 2 and escolhajogador == 1:
    print('COMPUTADOR VENCE')
