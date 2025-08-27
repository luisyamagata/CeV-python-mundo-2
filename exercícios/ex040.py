a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
m = (a+b)/2
print(m)
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(a, b, m))
if m >= 7.0:
    print('O aluno está APROVADO.')
elif 7 > m >= 5:
    print('Aluno em RECUPERAÇÃO')
elif m < 5:
    print('Aluno REPROVADO')
