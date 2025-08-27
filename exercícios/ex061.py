print('Gerador de PA')
print('-='*10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
pa = []
contador = 1
an = a1
# an = an-1+r
while contador < 11:
    an = a1 + (r * contador)
    print(an, '→', end=' ')
    contador +=1
print('FIM')

