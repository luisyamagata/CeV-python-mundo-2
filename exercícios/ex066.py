n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        c = c + 1
    if n == 999:
        break
    s += n

print(s)
print(c)
print(f'A soma dos {c} valores foi {s}!')
