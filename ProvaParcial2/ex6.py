#Utilizando apenas função lambda e as funções map, reducee filter. Crie um script que some todas as 
#idades das pessoas com mais de 18 anos e menos que 30:

from functools import reduce


pessoas = [ {'nome': 'Pedro', 'idade': 11},
            {'nome': 'Mariana', 'idade': 18},
            {'nome': 'Arthur', 'idade': 26},
            {'nome': 'Rebeca', 'idade': 6},
            {'nome': 'Raquel', 'idade': 34},
            {'nome': 'André', 'idade':22},
            {'nome': 'Tiago', 'idade': 19},
            {'nome': 'Gabriela', 'idade': 127}]

#Soma das idades entre 18 e 30 anos

idades_desejadas = list(filter(lambda p: p['idade'] > 18 and p['idade'] < 30, pessoas))
print(list(idades_desejadas))

print('---------------')

soma_idades = reduce(lambda idade, pessoa: idade + pessoa['idade'], idades_desejadas, 0)
print(soma_idades)


