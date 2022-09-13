
lista = []
print(type(lista))

print(len(lista))

lista.append(1)
lista.append(5)
print(lista)

print(lista[0])
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia', ['C#', 'Python', 'Node'], 3.14]
print(nova_lista)

print(nova_lista[3])
print(nova_lista[4])
print(nova_lista[4][1][3])
print(nova_lista[4][0][1])

nova_lista.remove(5)
print(nova_lista)

nova_lista.reverse()
print(nova_lista)

listaa = [1, 5, 'Raquel', 'Guilherme', 3.1415, 'Guilherme']

print(listaa.index(5))
print(listaa.index('Raquel'))
print(listaa.index('Guilherme'))
print('Andre' in listaa)
print('Raquel' in listaa)


listaa.append('Andre')
print(listaa)

listaa.insert(2, 'Ana')
print(listaa)

listaa.insert(2, ['Metallica', 'Led', 'Ozzy'])
print(listaa)

pop = ['Ana', 'Aline', 'Guilherme', 'Andre', 'Dani']
print(pop[1:3])
print(pop[1:-1])
print(pop[1:])