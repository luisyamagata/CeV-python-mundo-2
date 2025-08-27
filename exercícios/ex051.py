print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1
for c in range (1, 10, 1):
    an = a1 + (r * c)
    print(an, '→', end=' ')
print('ACABOU')
