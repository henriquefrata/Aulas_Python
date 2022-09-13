a = int(input('Digite o valor: '))
#print(a)
#print(type(a))
b = int(input('Digite o valor: '))
c = int(input('Digite o valor: '))

resultado = 0

if a > b and a > c:
    resultado = a
elif b > c and b > a:
    resultado = b
else:
    resultado = c

print(resultado)