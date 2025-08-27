#calcule a soma de todos os ímpares números múltiplos de 3 que estão no intervalo entre 1 e 500
#testando com 1 a 50
numeros = [ ]
for c in range(3,501,6):
    numeros.append(c)
print(numeros)
soma = sum(numeros)
itens = len(numeros)
print('A soma de todos os {} valores solicitados é {}'.format(itens, soma))
