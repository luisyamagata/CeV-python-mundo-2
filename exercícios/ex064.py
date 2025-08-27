n = 0
soma = 0
contador = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma = soma + n
        contador = contador + 1
print(soma)
print(contador)
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')