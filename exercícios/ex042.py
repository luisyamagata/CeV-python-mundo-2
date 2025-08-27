a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print(a, b, c)
if a<b+c and b<a+c and c<a+b:
    print('Esses segmentos formam um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a !=b and a!=c and b != c:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Esses segmentos NÃO PODEM FORMAR um triângulo')
