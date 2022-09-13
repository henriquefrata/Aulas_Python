from subprocess import list2cmdline


x = int(input('digite: '))
lista = []
lista.append(0)
lista.append(1)


for number in range(2, 9+x):
    # item autal = item atual - 1 + item atual - 2
    lista.append(lista[number - 1] + lista[number - 2])

print(lista[x-1:])