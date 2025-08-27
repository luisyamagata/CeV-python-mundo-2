import random
print('Sou seu computador...')
num_cpu = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite? '))
contador_palpites = 1
while palpite != num_cpu:
    if palpite < num_cpu:
        palpite = int(input('Mais... Tente mais uma vez. '))
        contador_palpites += 1
    elif palpite > num_cpu:
        palpite = int(input('Menos... Tente mais uma vez. '))
        contador_palpites += 1
print(f'Acertou com {contador_palpites} tentativas. Parabéns!')
