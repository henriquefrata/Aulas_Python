pessoa = {}
print(type(pessoa))

pessoa = {'nome': 'Andre', 'idade': 35, 'altura': 1.83}
print(pessoa)
print(pessoa['idade'])
print(pessoa['nome'])

pessoa = {'nome': 'Andre', 'idade': 35, 'altura': 1.83, 'cursos': ['C#', 'Node', 'React', 'Python']}
print(pessoa)
print(pessoa['altura'])
print(pessoa['cursos'])
print(pessoa['cursos'][2])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
items = list(pessoa.items())
print(items)

print(items[2])
print(type(items))
print(items[3])
print(type(items[3]))
print(items[3][1])
print(type(items[3][1]))
print(items[3][1][2])
print(type(items[3][1][2]))
print(items[3][1][2][1])
print(type(items[3][1][2][1]))

lista_pessoas = [{'nome': 'Andre', 'idade': 35, 'altura': 1.83},
                 {'nome':'Ana','idade':22, 'altura':1.57},
                 {'nome': 'João', 'idade': 39, 'altura': 1.78},
                 {'nome': 'Bia', 'idade': 27, 'altura': 1.63}]

print(lista_pessoas[2]['idade'])

pessoa1 = {'nome': 'Andre', 'idade': 35, 'altura': 1.83}

pessoa1.update({'idade':34, 'genero':'M'})
print(pessoa1)