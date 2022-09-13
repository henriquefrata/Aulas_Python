from random import randint

x = int(input('Digite o valor que você acredita ser o certo: '))

y = randint(0,9)

while x != y:
    x = int(input('Digite o valor que você acredita ser o certo: '))

print(f'O número secreto {y} foi encontrado')